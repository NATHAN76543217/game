var MySaves;(function(n){function ct(){if(sj_evt.bind("ClientLinkAction_Loaded",bt,!0),t&&(e.bind(t,w,function(){return h(f.Long)}),e.bind(t,et,function(){return h(f.Short)}),e.bind(_d.body,w,vt),e.bind(_d.body,ot,yt)),it()&&at(),t){var n=parseInt(lt(t,"padding"))||0;v=Math.floor(n)}}function lt(n,t){if(typeof MMUtilsStyle!="undefined"&&MMUtilsStyle.gcsv)return MMUtilsStyle.gcsv(n,t)}function at(){var n=i.gfbc("infact",_ge("vmc")),t,r;n&&n.firstChild&&(t=n.firstChild,r=t.getAttribute("data-tooltip"),r==ft&&t.setAttribute(y,"1"))}function vt(t){var r=sj_et(t),i=tt(r);i&&(n.selectedElement=i,o==null&&s(i))}function yt(t){var f=t.keyCode,r,i,u;f===ht&&(r=sj_et(t),i=tt(r),i?(n.selectedElement=i,s(i),wt(),nt(t)):r==g&&(u=pt(n.selectedElement),u&&(u.focus(),nt(t))))}function pt(n){var r,t,i;if(n&&(r=u(n,"infsec"),r&&(t=r.getElementsByTagName("A"),t&&t.length>1)))for(i=0;i<t.length;i++)if(t[i]==n.parentElement&&i<t.length-1)return t[i+1];return null}function nt(n){sj_pd(n);sj_sp(n)}function wt(){var n,i;t&&(n=t.getElementsByTagName("A"),n&&n.length>1&&(i=n[0],i.focus(),g=n[1]))}function tt(n){var r,i;if(n){if(r=u(n,"ms_ba_op"),r&&r.parentElement==t)return null;if(i=n.parentNode,i&&i.hash&&i.hash.indexOf(k)===0)return i;if(n.hash&&n.hash.indexOf(k)===0)return n}return null}function bt(n){if(n&&n[1]){var t=n[1];t.bind("Save",kt,!0);t.bind("Unsave",ti,!0);t.bind("OnMoveTo",dt,!0)}}function kt(t){var i=l(t);i&&(n.saveFunction(i,function(n){n&&n.IsSuccess||c(!1,t)}),n.selectedElement=t,(!_w.MySavesEdu||MySavesEdu.doneFiring)&&s(t),clearTimeout(o),o=setTimeout(function(){o=null},1500),c(!0,t));FavLog.l(FavLog.Type.Click,FavLog.Meta.Save,n.componentType)}function dt(t){n.abstractOnMoveTo(t)}function gt(){var n=parseQueryParams().q;return{title:n?decodeURI(n):null}}function s(n,u){var g,w,nt,tt,it,l,y;if(u===void 0&&(u="down"),t&&n&&!(ut()&&n.id==="mb_fav")){r&&clearTimeout(r);var e=n.getBoundingClientRect(),b="Top",k=sj_go(n,b),p=sj_go(_ge("vm_c"),b),ft=_w.innerHeight;(rt()||ut()&&d)&&(p+=sj_go(d,"Top"));switch(u){case"up":i.sb(t,ft-k+p);break;case"down":default:i.st(t,k+e.height-p)}var s="",o="",c=_d.body.offsetWidth;c-e.right>200?(g=5,o=Math.max(e.right-100+_w.pageXOffset,g-e.left),rt()&&(o-=st.getBoundingClientRect().left,o<0&&(o=0))):(s=c-e.right-60+_w.pageXOffset,o="",s<0&&(s=0),w=t.getBoundingClientRect(),nt=w.width<250?250:w.width,nt+s>c&&(s="",o=10));i.sr(t,s);i.sl(t,o);a&&(tt=parseInt(s),it=parseInt(o),isNaN(tt)?isNaN(it)||(y=o+v-e.left+e.width/2,y=Math.floor(y),i.sl(a,y)):(l=c-s-v-e.right+e.width/2,l=Math.floor(l),i.sr(a,l)));i.sdt(t,DisplayType.InlineBlock);r=setTimeout(function(){h(f.Short)},1)}}function it(){var n=_w.location.href.toLowerCase();return n.indexOf("&testhooks=~1")>0&&n.indexOf("&vpt=1")>0}function ni(){var n=i.gebc("mystuff",_d)[0];n&&i.ac(n,y)}function h(u){r?clearTimeout(r):FavLog.l(FavLog.Type.Show,FavLog.Meta.ShowBalloon,n.componentType);i.ac(t,b);sj_evt.fire("MySavesBalloon.show");var f=function(){i.rc(t,b);sj_evt.fire("MySavesBalloon.hide");r=setTimeout(function(){t&&i.sdt(t,DisplayType.Default);n.selectedElement=null;r=null},500)};it()||(ni(),r=setTimeout(f,u))}function ti(u){var f=l(u);f||(f=l(n.selectedElement),u=n.selectedElement);f&&(n.unsaveFunction(f,function(n){n&&n.IsSuccess||c(!0,u)}),c(!1,u),t&&(r&&clearTimeout(r),i.sdt(t,DisplayType.Default)));FavLog.l(FavLog.Type.Click,FavLog.Meta.Unsave,n.componentType)}function c(n,t){if(t){var r=u(t,"iuscp")||u(t,"iuscwrapper");r&&(n?i.ac(r,p):i.rc(r,p))}}function l(t){if(t){if(typeof MySavesMetadataProvider!="undefined")return MySavesMetadataProvider.getMetadata(t);if(t=u(t,"iuscp"),t)return JSON.parse(i.ga(t.querySelector(".iusc"),"m"))}else if(typeof n.contextMetadata!="undefined")return n.contextMetadata;return null}function u(n,t){while(n){if(i.hc(n,t))return n;n=n.parentElement}return null}function rt(){return typeof ImageDetailV2!="undefined"&&ImageDetailV2.isRightRailShown()}function ut(){return typeof MobileImageDetail!="undefined"}var f;(function(n){n[n.Short=3e3]="Short";n[n.Long=99999]="Long"})(f=n.AnimationTimeout||(n.AnimationTimeout={}));var y="vptest",ft="Save this",p="saved",w="mouseover",et="mouseout",ot="keydown",e=SmartEvent,i=pMMUtils,r,b="show",k="#CA!Unsave",d=_ge("insights"),st=_ge("insights_wrap"),o=null,t=_ge("ms_ba"),a=_ge("ms_ba_ar"),ht=9,g=null,v=0;n.init=ct;n.abstractOnMoveTo=function(){return null};n.getSpecifier=gt;n.showBalloon=s;n.setBalloonVisible=h;n.getMetadata=l})(MySaves||(MySaves={}));MySaves.init()