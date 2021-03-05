---
title: "GoldenDict 插件化 '碑'记"
date: 2020-06-06T01:20:30+08:00
draft: true
tags: [GoldenDict,Qt]
categories: [GoldenDict,Qt]
---
### 抽丝剥茧，由外及内 --- 合久必分，分久必合 --- 按需加载，资源不浪费，问题不易出
>插件测试程序：[GoldenDict_plugins_test.7z](https://forum.freemdict.com/uploads/short-url/lGCATiNK93yC9baAZiotXksZuHz.7z) (19.8 MB) 
![截图|371x499](https://forumcdn.freemdict.com/uploads/default/original/2X/7/73592fdf951accc958d41312ff45a69d38fa201b.png) 
### 1. 插件公共接口
```c++
class GDCORE_EXPORT GDPObject : public QObject
{
    Q_OBJECT
public:
    explicit GDPObject(QObject *parent = nullptr) : QObject(parent), owner(nullptr)
    {}
    virtual ~GDPObject()
    {}

    virtual int type() const = 0; /*GDO_Type*/
    virtual QString name() const = 0;
    virtual QString author() const = 0;

    virtual bool init() = 0;

    int version() const;
    QString fileName() const;

    static QList<QPair<QString/*iid*/, QString/*path*/> > metaInfo(const QString &dir, const QString filter);
    static GDPObject* loadObject(const QString &file, QObject *parent = nullptr);

    void unload();/* owner deletelater */

signals:
  void error( const QString& );

private:
    class GDPObjOwner;
    GDPObjOwner *owner;
};
```
### 2. AudioPlayer公共接口
```c++
class GDPAudioPlayer : public GDPObject
{
public:
    explicit GDPAudioPlayer(QObject *parent = nullptr) : GDPObject(parent)
    {}
    virtual ~GDPAudioPlayer()
    {}


    int type() const {  return GDOT_AudioPlayer;  }

    /// Initialize audio device and playback environment
    //virtual bool init() = 0;
    /// Stops current playback if any, copies the audio buffer, then plays the duplication.
    /// Returns an error message in case of immediate failure; an empty string in case of success.
    virtual QString play( const QByteArray &audioBuffer ) = 0;
    virtual QString playFile( const QString &file ) = 0;
    /// Stops current playback if any.
    virtual void stop() = 0;

};
#define GDPAudioPlayer_iid "gdp.AudioPlayer"
Q_DECLARE_INTERFACE(GDPAudioPlayer, GDPAudioPlayer_iid)
```
AudioPlayer插件实例：
```c++
class QtMediaplayer : public GDPAudioPlayer
{
    Q_OBJECT
#if (QT_VERSION >= QT_VERSION_CHECK(5, 0, 0))
    Q_PLUGIN_METADATA(IID "adp/Qt Multimedia")
    Q_INTERFACES(GDPAudioPlayer)
#endif
public:
    QtMediaplayer();
    ~QtMediaplayer();

    bool init() override;

    QString name() const {  return tr("Qt Multimedia");  }
    QString author() const {  return "GoldenDict Official";  }

    QString play( const QByteArray &_audioBuffer ) override;
    QString playFile( const QString &file ) override;
    void stop() override;

private slots:
  void onMediaPlayerError(QMediaPlayer::Error);

private:
    QMediaPlayer *player; ///< Depends on audioBuffer.
    QBuffer audioBuffer;

};
```

```c++
QtMediaplayer::QtMediaplayer() : GDPAudioPlayer(),
  player(0)
{
}

QtMediaplayer::~QtMediaplayer()
{
    if(player)
        delete player;
}

bool QtMediaplayer::init()
{
    player = new QMediaPlayer(nullptr, QMediaPlayer::StreamPlayback );
    connect( player, SIGNAL(error(QMediaPlayer::Error)),
             this, SLOT(onMediaPlayerError(QMediaPlayer::Error)) );
    return true;
}

QString QtMediaplayer::play(const QByteArray &_audioBuffer)
{
    if(player)
    {
        stop();
        audioBuffer.setData( _audioBuffer );
        if( !audioBuffer.open( QIODevice::ReadOnly ) )
            return tr( "Couldn't open audio buffer for reading." );

        player->setMedia( QMediaContent(), &audioBuffer );
        player->play();
    }
    return QString();
}

QString QtMediaplayer::playFile( const QString &file )
{
    if(player)
    {
        stop();
        player->setMedia( QMediaContent(QUrl::fromLocalFile(file)) );
        player->play();
    }
    return QString();
}

void QtMediaplayer::stop()
{
    if(player)
    {
        player->setMedia( QMediaContent() ); // Forget about audioBuffer.
        if(audioBuffer.isOpen()) {
            audioBuffer.close();
            audioBuffer.setData( QByteArray() ); // Free memory.
        }
    }
}

void QtMediaplayer::onMediaPlayerError(QMediaPlayer::Error err)
{
  QString errstr = player->errorString();
  if(errstr.isEmpty())
    errstr = tr("Error==%1").arg(err);
  emit error( errstr );
}

#if (QT_VERSION < QT_VERSION_CHECK(5, 0, 0))
Q_EXPORT_PLUGIN(QtMediaplayer)
#endif
```
### 3. OCR划词共接口
```c++
class GDPOcrText : public GDPObject
{
public:
    typedef QList<QPair<QString/*id*/, QString/*name*/> > OCR_LAN;
    typedef QMap<QString /*area*/, OCR_LAN > OCR_LANS;
public:
    explicit GDPOcrText(QObject *parent = nullptr) : GDPObject(parent)
    {}
    virtual ~GDPOcrText()
    {}

    int type() const {    return GDOT_OcrWords;    }

    virtual void enableLans(const QStringList &lans, const QString &area) = 0;
    virtual OCR_LANS getAreaLans() const = 0;
    virtual void setDataPath(const QString &datadir) = 0;
    virtual QString dataPath() const = 0;

    virtual void ocrScreen() = 0;
    virtual void ocrMemory(const QByteArray &bmpdata) = 0; /* bmp data */
    virtual void ocrFile(const QString &file) = 0;

    virtual bool isWorking() const = 0;
    virtual void stop() = 0;
};
#define GDPOcrObject_iid "gdp.OcrText"
Q_DECLARE_INTERFACE(GDPOcrText, GDPOcrObject_iid)
```