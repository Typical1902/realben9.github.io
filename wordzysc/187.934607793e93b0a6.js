"use strict";(self.webpackChunkcm=self.webpackChunkcm||[]).push([[187],{34187:(D,h,n)=>{n.r(h),n.d(h,{AvatarModule:()=>B});var d=n(59516),m=n(15689),p=n(3894),r=n(82370),u=(n(65428),n(83244)),A=n(92773),C=n(98471),t=n(5e3),x=n(12011),S=n(13264),y=n(49257),w=n(77836),v=n(69808),g=n(77093),T=n(47423);function Z(a,i){1&a&&(t.TgZ(0,"div",8),t._uU(1,"Sign in"),t.qZA())}function Y(a,i){1&a&&(t.TgZ(0,"div",9),t._uU(1,"for avatar"),t.qZA())}function U(a,i){1&a&&(t.TgZ(0,"div"),t._uU(1,"Signing in ..."),t.qZA())}function J(a,i){if(1&a){const e=t.EpF();t.TgZ(0,"div",3)(1,"button",4),t.NdJ("click",function(o){return t.CHM(e),t.oxw().login(o)}),t.YNc(2,Z,2,0,"div",5),t.YNc(3,Y,2,0,"div",6),t.YNc(4,U,2,0,"div",2),t.qZA(),t.TgZ(5,"p",7),t._uU(6,"Avatar is only available for registered users."),t.qZA()()}if(2&a){const e=t.oxw();t.xp6(1),t.Q6J("ngSwitch",e.loginService.isLoggingIn())("disabled",e.loginService.isLoggingIn()),t.xp6(1),t.Q6J("ngSwitchCase",!1),t.xp6(1),t.Q6J("ngSwitchCase",!1),t.xp6(1),t.Q6J("ngSwitchCase",!0)}}function Q(a,i){1&a&&(t.TgZ(0,"div")(1,"p",12),t._uU(2,"Sorry, you don't have enough coins needed to save a new avatar!"),t.qZA()())}function L(a,i){1&a&&t._UZ(0,"iframe",13)}function R(a,i){if(1&a&&(t.ynx(0),t.YNc(1,Q,3,0,"div",10),t.YNc(2,L,1,0,"iframe",11),t.BQk()),2&a){const e=t.oxw();t.xp6(1),t.Q6J("ngIf",e.noCoins),t.xp6(1),t.Q6J("ngIf",e.isReady)}}const N=[{path:"",component:(()=>{class a{constructor(e,s,o,c,l){this.router=e,this.firebaseApp=s,this.cacheService=o,this.dataService=c,this.loginService=l,this.noCoins=!1,this.hasCost=!1,this.isReady=!1,this.setReady()}setReady(){if(!this.cacheService.hasFirebase()||!this.cacheService.firebaseCache.self.pvt.hasData())return void setTimeout(()=>this.setReady(),500);window["reload-avatar"]=()=>{window["load-avatar"]=void 0,document.getElementById("avatar").src+=""};const e=this.cacheService.firebaseCache.self.pvt.getAvatarParams();if(this.hasCost=!!e,!this.hasCost){const c=this.cacheService.firebaseCache.self.meta.getUrl();c&&c.indexOf("http")>=0&&(this.hasCost=!0)}const s=this.cacheService.firebaseCache.self.meta.getCoins();let o=(0,C.vY)(s);this.hasCost&&s<o?this.noCoins=!0:(window["save-msg"]="save"+(this.hasCost?" ("+A.L.transform(o)+")":""),window["load-avatar"]=e,window["save-avatar"]=(c,l,V)=>{const F="/pic/"+this.loginService.getFirebaseUid(),f=this.firebaseApp.storage().ref().child(F);f.put(function I(a){const i=atob(a.split(",")[1]),e=a.split(",")[0].split(":")[1].split(";")[0],s=new Uint8Array(i.length);for(let o=0;o<i.length;o++)s[o]=i.charCodeAt(o);return new Blob([s],{type:e})}(c),{cacheControl:"public,max-age=31536000",contentType:"image/png"}).then(z=>{window["load-avatar"]=l,f.getDownloadURL().then(M=>{this.hasCost&&!this.dataService.chargeCoins(u.UV.AVATAR,"Avatar",o)||(this.cacheService.firebaseCache.self.setAvatar(M,l),this.router.navigateByUrl("/Profile"),r.c.trackEvent(r.c.Action.Avatar,r.c.Action.Done))})})},this.isReady=!0)}login(e){this.loginService.login(e),r.c.trackEvent(r.c.Action.Avatar,r.c.Action.Login)}}return a.\u0275fac=function(e){return new(e||a)(t.Y36(d.F0),t.Y36(x.Ot),t.Y36(S.Q),t.Y36(y.D),t.Y36(w.r))},a.\u0275cmp=t.Xpm({type:a,selectors:[["cm-avatar"]],decls:3,vars:3,consts:[[1,"core",3,"ngSwitch"],["fxLayout","column","fxLayoutAlign","center center","class","padded","style","text-align: center; margin-top: 16px;",4,"ngSwitchCase"],[4,"ngSwitchCase"],["fxLayout","column","fxLayoutAlign","center center",1,"padded",2,"text-align","center","margin-top","16px"],["color","green","mat-raised-button","",1,"signin",3,"ngSwitch","disabled","click"],["class","line1",4,"ngSwitchCase"],["class","line2",4,"ngSwitchCase"],[1,"sec-fade",2,"max-width","180px","text-align","center"],[1,"line1"],[1,"line2"],[4,"ngIf"],["id","avatar","src","svgavatars.html","height","1000","width","100%","scrolling","no","frameborder","0",4,"ngIf"],[2,"text-align","center","font-size","18px","padding-top","48px"],["id","avatar","src","svgavatars.html","height","1000","width","100%","scrolling","no","frameborder","0"]],template:function(e,s){1&e&&(t.TgZ(0,"div",0),t.YNc(1,J,7,5,"div",1),t.YNc(2,R,3,2,"ng-container",2),t.qZA()),2&e&&(t.Q6J("ngSwitch",s.loginService.isLoggedIn()),t.xp6(1),t.Q6J("ngSwitchCase",!1),t.xp6(1),t.Q6J("ngSwitchCase",!0))},directives:[v.RF,v.n9,g.xw,g.Wh,T.lW,v.O5],encapsulation:2}),a})()}];let B=(()=>{class a{}return a.\u0275fac=function(e){return new(e||a)},a.\u0275mod=t.oAB({type:a}),a.\u0275inj=t.cJS({imports:[[m.TE,p.m,d.Bz.forChild(N)]]}),a})()}}]);