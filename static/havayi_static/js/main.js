

var body = document.querySelector('body')
    var body_height = $(body).height()
    var window_height = $(window).height()

    
if (body_height < window_height) {
    let end = document.querySelector('.service-end')
    console.log(end)
    end.classList.add('position-absolute')
    end.style.bottom = '0';
}

var mobile_menu = document.querySelector('.mobile-menu');

var exit_figure_img = document.querySelector('.exit-figure-img');


console.log('aa')
document.querySelector('body').addEventListener('click', function (event) {
    console.log('1')
    if (mobile_menu.classList.contains('view-mobile-menu')) {
        console.log('2')
        if (event.target.id === 'exit-figure-img') {
            mobile_menu.classList.remove('view-mobile-menu');
        } else if (event.target.closest('.view-mobile-menu')) {
            mobile_menu.classList.add('view-mobile-menu');
        }
        else {
            mobile_menu.classList.remove('view-mobile-menu');
        }
    }
    else{
        console.log('3')
        if (event.target.id === 'hamburger'){
            console.log('4')
            mobile_menu.classList.add('view-mobile-menu');
        }
    }
})
