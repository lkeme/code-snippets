## 网抑云批量删动态

```js
lists = document.getElementsByClassName("li f-fl s-fc3")
for(i in lists) {
   lists[i].click();
   document.getElementsByClassName("u-btn2 u-btn2-2 u-btn2-w2")[0].click();
}
```