var FlagFeedback;(function(n){function g(n){n=n||window.event;var t=n.target||n.srcElement;i&&!i.contains(t)&&i.offsetHeight>0&&y()}function nt(n){var t,r;n=n||window.event;t=n.target||n.srcElement;i&&i.contains(t)&&(r=n?n.which?n.which:n.keyCode:n.keyCode,r==ft?(t.tagName=="INPUT"||t.className=="buttonLink"||t.id=="fbdialogcl")&&t.click():r==et?(t.className=="buttonLink"||t.id=="fbdialogcl")&&(t.click(),a(n)):r==ot&&(y(),a(n)))}function tt(n){l&&!i.contains(n.target)&&(a(n),i.focus())}function a(n){sj_sp(n);sj_pd(n)}function v(){sj_ue(_d,"click",g);sj_ue(_d,"keydown",nt);sj_ue(_d,"focusin",tt);sj_evt.unbind("ajax.unload",v)}function st(){c=document.activeElement;var n=this.metadata;n&&ht(n.turl,n.maw,n.mah)}function ht(n,t,r){f.innerHTML="";var e=_d.createElement("img");e.src=n;t&&r&&(t>250?(e.width=250,e.height=r*250/t):(e.width=t,e.height=r));f.appendChild(e);i.style.display="block";l=!0;u.focus()}function ct(){(u.checked||e.checked||o.checked||s.checked)&&(t.style.display="none",t.innerHTML="",t.setAttribute(h,"true"))}function y(){i.style.display="none";p.style.display="block";r.style.display="none";r.innerHTML="";f.style.display="block";t.style.display="none";t.innerHTML="";t.setAttribute(h,"true");b.style.display="block";k.style.display="block";d.style.display="none";u.checked=!1;e.checked=!1;o.checked=!1;s.checked=!1;var n=this.metadata;n&&it("flagClose",null,n.ns,n.k);l=!1;c&&c.focus();sj_evt.fire(ut)}function lt(){var i,r,n,f;if(!u.checked&&!e.checked&&!o.checked&&!s.checked){t.style.display="block";t.innerHTML=t.dataset.content;t.setAttribute(h,"false");t.focus();return}if(i=[],u.checked&&i.push("irrelevant"),e.checked&&i.push("offensive"),o.checked&&i.push("adult"),s.checked&&i.push("childabuse"),r=i.join(","),n=this.metadata,n&&(it("flagSubmit",r,n.ns,n.k),f=w.getAttribute("fbposturl"),f)){var c=window.location.href.match("(images|videos)"),a=c?c[0]:"",l=window.location.href.match(/q=(.+?)(&|$)/),v=l?l[1]:"",y=w.getAttribute("ss"),p=!!n.md5&&n.md5.length>0?n.md5:null;ReportResult.send(f,a,v,"External",encodeURIComponent(n.imgurl),encodeURIComponent(n.surl),encodeURIComponent(n.turl),p,null,r,n.src,y)}at()}function it(n,t,i,r){if(typeof mmLog!="undefined"&&mmLog){var u=['{"T":"CI.Click","Name":"',n,'","Meta":"',t,'","AppNS":"',i,'","K":"',r,".1",'","TS":',sb_gt(),"}"];mmLog(u.join(""))}}function at(){p.style.display="none";r.style.display="block";r.innerHTML=r.dataset.content;f.style.display="none";b.style.display="none";k.style.display="none";d.style.display="block";rt.focus()}var h="aria-hidden",i=_ge("fbdialog"),p=_ge("fbdialog_message"),r=_ge("fbthankyou_message"),w=_ge("fbdialog_container"),f=_ge("fbdialog_thumb_container"),t=_ge("fbdialog_errormessage"),b=_ge("checkbox_region"),u=_ge("irrelevant_mark_checkbox"),e=_ge("offensive_mark_checkbox"),o=_ge("adult_mark_checkbox"),s=_ge("childabuse_mark_checkbox"),k=_ge("fbdialog_buttons"),d=_ge("fbthankyou_button"),rt=_ge("adult_button_close"),ut="flagfeedback_close",ft=13,et=32,ot=27,c,l=!1;sj_be(_d,"click",g);sj_be(_d,"keydown",nt);sj_be(_d,"focusin",tt);sj_be(_d,"unload",v);sj_evt.bind("ajax.unload",v);n.c=st;n.p=ct;n.s=lt;n.h=y})(FlagFeedback||(FlagFeedback={}))