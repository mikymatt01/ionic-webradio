# ionic-webradio
A project to create a personal web radio and ionic app
This project is the source code of a tutorial on how to build an Ionic Radio Player.

[![](https://mermaid.ink/img/eyJjb2RlIjoic3RhdGVEaWFncmFtXG5weXRob25fc2NyaXB0LS0-IHdpbmFtcFxucHl0aG9uX3NjcmlwdCAtLT4gU2hvdXRjYXN0XG5weXRob25fc2NyaXB0LS0-IG5ncm9rXG53aW5hbXAgLS0-IFNob3V0Y2FzdFxuU2hvdXRjYXN0IC0tPiBuZ3Jva1xubmdyb2stLT4gaW9uaWNfYXBwMVxubmdyb2stLT4gaW5vY19hcHAyXG5uZ3Jvay0tPiBpb25pY19hcHAzXG5cdFx0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid.ink/img/eyJjb2RlIjoic3RhdGVEaWFncmFtXG5weXRob25fc2NyaXB0LS0-IHdpbmFtcFxucHl0aG9uX3NjcmlwdCAtLT4gU2hvdXRjYXN0XG5weXRob25fc2NyaXB0LS0-IG5ncm9rXG53aW5hbXAgLS0-IFNob3V0Y2FzdFxuU2hvdXRjYXN0IC0tPiBuZ3Jva1xubmdyb2stLT4gaW9uaWNfYXBwMVxubmdyb2stLT4gaW5vY19hcHAyXG5uZ3Jvay0tPiBpb25pY19hcHAzXG5cdFx0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

## winamp
winamp is the radio's source that, through the SHOUTcast DSP plugin, will send the digital audio directly to a SHOUTcast streaming server 
## shoutcast
Shoutcast is the radio's server that will distribute the sound at app
## ngrok
ngrok exposes local Shoutcast server behind NATs and firewalls to the public internet over secure tunnels. This is necessary because shoutcast is hosted in http but if you use html audio with source shoutcast http in a website https, this source is updated from http to https and not run.
## python script
it is a script in python lenguage that initiates the radio in the event that it should be started at a specific time every day. Once you start daemon script, it reads the time updating every half second and when it reads time when the radio should be activated, it started another scirpt colled 'open.py' that started each radio's element. When daemon reads a closing time of the radio, it starts 'close.py' that killed each process of the radio.
### daemon.py
```
import datetime
import time
import subprocess

start=datetime.time(hours, minutes, seconds)
end=datetime.time(hours, minutes, seconds)

if __name__=="__main__":
	while True:
		time_only = datetime.datetime.now().time().replace(microsecond=0)
		print(time_only)
		if time_only == daemon_start:
			subprocess.Popen(["python", "open.py"])
		if time_only == daemon_end:
			subprocess.Popen(["python", "close.py"])
		time.sleep(0.5)
```
### open.py
```
import os
import time

ShoutcastPath=	'Path of Shoutcast'
WinampPath   =	'Path of Winamp'
NgrokPath    =  'Path of Ngrok'
CleverPath   =  'Path of Clever'

os.system('start ' + ShoutcastPath + 'sc_serv')
os.system('start ' + WinampPath	   + 'Winamp')
time.sleep(1)
os.chdir(CleverPath)
os.system('clever loadplay PlaylistName')
os.chdir(NgrokPath)
os.system('ngrok.exe http --subdomain=SubdomainChosen 8000')
```
### close.py
```
import os

os.system('TASKKILL /F /IM sc_serv.exe')
os.system('TASKKILL /F /IM winamp.exe')
os.system('TASKKILL /F /IM ngrok.exe')
```
## ionic radio app
Ionic Framework is an open source UI toolkit for building performant, high-quality mobile and desktop apps using web technologies — HTML, CSS, and JavaScript — with integrations for popular frameworks like Angular and React. To connect shoutcast radio to ionic app should create a ionic project and create or modify pages.
### radio.page.ts
```
  url:any;
  stream: any;
  promise: any;
  isAdded: boolean = false;
  result: any = [];
  
  constructor(
    public alertCtrl: AlertController,
    private http: HttpClient
  ) {
    this.url="https://<subdomainchosen>.ngrok.io/;stream.mp3";
    this.stream= new Audio(this.url);
}

  async play(){
    this.stream.play();
    var timeradio = <The Radio's Hour>;
    var time = new Date(Date.now()).getHours(); //get the hours
      this.promise=new Promise((resolve, reject) => {
        this.http.get(this.url) //a get request to the server
          .toPromise()
          .then(
            res => { // Success
              resolve();
              },
              msg=> { // Error
              reject(msg);
              if(timeradio!==time) //if the time doesn't corresponds at time of radio
                this.presentAlertTime();
              else 
                this.presentAlertNet();
              }
          );
      });
  }

  stop(){
    this.stream.pause();
  }

  state() {
    this.isAdded = !this.isAdded;
    if(this.isAdded===true)
      this.play();
    else
      this.stop();
  }

  async presentAlertTime() {
    const alert = await this.alertCtrl.create({
      header: 'Radio',
      message: 'The radio isn't online now. It will be avaiable at <hour chosen>',
      buttons: ['OK']
    });
    this.isAdded = !this.isAdded;
    await alert.present();
  }

  async presentAlertNet() {
    const alert = await this.alertCtrl.create({
      header: 'Radio',
      message: 'check your internet connection and try again',
      buttons: ['OK']
    });
    this.isAdded = !this.isAdded;
    await alert.present();
  }
}
```
### radio.page.html
```
<ion-fab vertical="bottom" horizontal="center" slot="fixed">
  <ion-fab-button (click)='state()' [color]="(isAdded) ? 'dark' : 'primary'"  size=''><ion-icon [name]="(isAdded) ? 'pause-outline' : 'play-outline'"></ion-icon></ion-fab-button>
  </ion-fab>
```
