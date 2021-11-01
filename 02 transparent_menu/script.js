console.log('%c hello 👋 ', 'background: #222; color: #ffc7ba; font-size:15px; line-height:30px; text-shadow:-1px -1px 0 #000,-1px 1px 0 #000,1px -1px 0 #000,1px 1px 0 #ae2d68; ');
console.log('date: 28 Oct 2021, time taken = about 2 hours');

function changeLang(btn) {
    var toHide, toShow;
    // console.log(btn)
    if (!btn) {
        toHide = document.querySelectorAll('[lang="zh"]');
        toShow = [];
    } else {
        lang = btn.value;
        
        if (lang === 'en') {
            // change to english to chinese
            btn.value = 'zh';
            toHide = document.querySelectorAll('[lang="en"]');
            // console.log(changes);
            toShow = document.querySelectorAll('[lang="zh"]');
            document.getElementsByTagName('body')[0].style.fontFamily = "'Ma Shan Zheng', cursive";
        } else if (lang === 'zh') {
            // change from chinese to english
            btn.value = "en";
            toHide = document.querySelectorAll('[lang="zh"]');
            toShow = document.querySelectorAll('[lang="en"]');
            document.getElementsByTagName('body')[0].style.fontFamily = "'Bree Serif', serif";
        }
    }
    
    for (var elm of toHide) {
        elm.style.display = 'none';
    };
    
    for (var elm of toShow){
        elm.style.display = '';
    }
}

document.addEventListener("DOMContentLoaded", function(event) {

    // add hover listener to menu links
    const bodyElem = document.getElementById('main');
    menuLinks = document.getElementsByClassName('menu-link');
    // console.log(menuLinks)
    var imgFileName;
    for (var element of menuLinks) {
        element.addEventListener('mouseover', function(event) {
            // console.log('id: ' + event.target.id);
            imgFileName = event.target.parentElement.id + '.png'
            bodyElem.style.backgroundImage = "url('./imgs/"+ imgFileName + "')";
            bodyElem.style.backgroundSize = 'cover';
        }, false);
        element.addEventListener('mouseout', function() {
            // console.log('mouseover')
            bodyElem.style.backgroundImage = "";
        }, false);
    }

    changeLang();
});
