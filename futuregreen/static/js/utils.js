function Square()
{
    $('.square').each(function(){
        width = $(this).width();
        $(this).css('height',width);
    });
    $('.center').each(function(){
        width = $(this).width();
        $(this).css('line-height',width + "px");
    });
 }


