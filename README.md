# ionic-webradio
A project to create a personal web radio and ionic app
This project is the source code of a tutorial on how to build an Ionic/Phonegap Radio Player and display any information which is provided by the SHOUTcast stream server.

[![](https://mermaid.ink/img/eyJjb2RlIjoic3RhdGVEaWFncmFtXG5cdFdpbmFtcCAtLT4gU2hvdXRjYXN0XG5cdFNob3V0Y2FzdCAtLT4gbmdyb2tcblx0bmdyb2sgLS0-IGlvbmljX2FwcDFcbiAgbmdyb2sgLS0-IGlvbmljX2FwcDJcbiAgbmdyb2sgLS0-IGlvbmljX2FwcDMgXG5cdFx0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifX0)](https://mermaid.ink/img/eyJjb2RlIjoic3RhdGVEaWFncmFtXG5cdFdpbmFtcCAtLT4gU2hvdXRjYXN0XG5cdFNob3V0Y2FzdCAtLT4gbmdyb2tcblx0bmdyb2sgLS0-IGlvbmljX2FwcDFcbiAgbmdyb2sgLS0-IGlvbmljX2FwcDJcbiAgbmdyb2sgLS0-IGlvbmljX2FwcDMgXG5cdFx0XHRcdFx0IiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifX0)

## winamp
winamp is the radio's source that, through the SHOUTcast DSP plugin, will send the digital audio directly to a SHOUTcast streaming server 
## shoutcast
Shoutcast is the radio's server that will distribute the sound at app
## ngrok
ngrok exposes local Shoutcast server behind NATs and firewalls to the public internet over secure tunnels. This is necessary because shoutcast is hosted in http but if you use html audio with source shoutcast http in a website https, this source is updated from http to https and not run.
## ionic radio app
Ionic Framework is an open source UI toolkit for building performant, high-quality mobile and desktop apps using web technologies — HTML, CSS, and JavaScript — with integrations for popular frameworks like Angular and React.
