###网易读私信

```js
let thide = document.getElementsByClassName("f-thide")
for (var i=0;i<thide.length;i++)
{ 
    thides = document.getElementsByClassName("f-thide");
    (thides[i]).click();
    window.history.back();
    console.log("完成第"+ i +"页")
}
window.history.go(-1); 
```