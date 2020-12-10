var left_side_menu = document.querySelector('.left-side-menu')

document.querySelector('body').addEventListener('click', function (event) {
    console.log('1')
    if (left_side_menu.classList.contains('clicking-menu')) {
        console.log('2')
        if (event.target.closest('.down-arrow-menu')) {
            left_side_menu.classList.remove('clicking-menu');
            document.querySelector('.arrow-icon').style.transform="rotate(0deg)"
        } else if (event.target.closest('.clicking-menu')) {
            left_side_menu.classList.add('clicking-menu');
            document.querySelector('.arrow-icon').style.transform="rotate(180deg)"
        }
        else {
            left_side_menu.classList.remove('clicking-menu');
            document.querySelector('.arrow-icon').style.transform="rotate(0deg)"
        }
    }
    else{
        console.log('3')
        if (event.target.closest('.down-arrow-menu')){
            console.log('4')
            left_side_menu.classList.add('clicking-menu');
            document.querySelector('.arrow-icon').style.transform="rotate(180deg)"
        }
    }
})