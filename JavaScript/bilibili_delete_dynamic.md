## 破站批量删除动态

```js
// 域名: space.bilibili.com

var needDelDeled = true,
    delay = 1000,
    scrolls = 800;
var w = '', d = '', r = 0;
function getLuckyDraw() {
    w.css("background-color", "#f1c40f");
    w = w.parents(".card");
    w.css("background-color", "#2ecc71");
    w[w.length - 1].querySelectorAll(".child-button")[1].click();
    setTimeout(clickDel, delay);
}
function getDel() {
    d.css("background-color", "#8e44ad");
    d = d.parents(".card");
    d.css("background-color", "#2ecc71");
    d[d.length - 1].querySelectorAll(".child-button")[1].click();
    setTimeout(clickDel, delay);
}
function clickDel() {
    //点删除
    $(".popup-content-ctnr")[$(".popup-content-ctnr").length - 2].querySelector(".bl-button").click(); // 点确定
    r += scrolls;
    $('html, body').animate({ scrollTop: r }, 30);
    $(".fold-text").click()
    $(".expand-btn").click();
    w = $(".main-content").find('span[click-title="抽奖详情"]');
    d = $(".main-content").find('.deleted-text');
    if (d.length && needDelDeled) setTimeout(getDel, delay);
    else setTimeout(getLuckyDraw, delay);
}
if (/dynamic/.test(window.location.href) && confirm("是不是要删除抽奖动态")) {
    r += scrolls;
    $('html, body').animate({ scrollTop: r }, 30);
    $(".fold-text").click()
    $(".expand-btn").click();
    w = $(".main-content").find('span[click-title="抽奖详情"]');//*互动抽奖内容定位
    d = $(".main-content").find('.deleted-text');   //*已删除内容定位
    if (d.length && needDelDeled) setTimeout(getDel, delay);
    else setTimeout(getLuckyDraw, delay);
}
```