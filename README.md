# ionic-webradio
A project to create a personal web radio and ionic app
This project is the source code of a tutorial on how to build an Ionic/Phonegap Radio Player and display any information which is provided by the SHOUTcast stream server.

[![](https://mermaid.ink/img/eyJjb2RlIjoic3RhdGVEaWFncmFtXG5weXRob25fc2NyaXB0LS0-IHdpbmFtcFxucHl0aG9uX3NjcmlwdCAtLT4gU2hvdXRjYXN0XG5weXRob25fc2NyaXB0LS0-IG5ncm9rXG53aW5hbXAgLS0-IFNob3V0Y2FzdFxuU2hvdXRjYXN0IC0tPiBuZ3Jva1xubmdyb2stLT4gaW9uaWNfYXBwMVxubmdyb2stLT4gaW5vY19hcHAyXG5uZ3Jvay0tPiBpb25pY19hcHAzXG5cdFx0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)](https://mermaid.ink/img/eyJjb2RlIjoic3RhdGVEaWFncmFtXG5weXRob25fc2NyaXB0LS0-IHdpbmFtcFxucHl0aG9uX3NjcmlwdCAtLT4gU2hvdXRjYXN0XG5weXRob25fc2NyaXB0LS0-IG5ncm9rXG53aW5hbXAgLS0-IFNob3V0Y2FzdFxuU2hvdXRjYXN0IC0tPiBuZ3Jva1xubmdyb2stLT4gaW9uaWNfYXBwMVxubmdyb2stLT4gaW5vY19hcHAyXG5uZ3Jvay0tPiBpb25pY19hcHAzXG5cdFx0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZX0)

## winamp
winamp is the radio's source that, through the SHOUTcast DSP plugin, will send the digital audio directly to a SHOUTcast streaming server 
## shoutcast
Shoutcast is the radio's server that will distribute the sound at app
## ngrok
ngrok exposes local Shoutcast server behind NATs and firewalls to the public internet over secure tunnels. This is necessary because shoutcast is hosted in http but if you use html audio with source shoutcast http in a website https, this source is updated from http to https and not run.
## python script
it is a script in python lenguage that initiates the radio in the event that it should be started at a specific time every day. Once you start daemon script, it reads the time updating every half second and when it reads time when the radio should be activated, it started another scirpt colled 'open.py' that started each radio's element. When daemon reads a closing time of the radio, it starts 'close.py' that killed each process of the radio.
## ionic radio app
Ionic Framework is an open source UI toolkit for building performant, high-quality mobile and desktop apps using web technologies — HTML, CSS, and JavaScript — with integrations for popular frameworks like Angular and React.
