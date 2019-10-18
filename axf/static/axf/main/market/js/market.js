$(function(){
    $('#all_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
             $('#all_type_container').toggle();

    });
    $('#all_sort').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
            $('#all_sort_container').toggle();
    });
    $('.addShopping').click(function () {
        var $button = $(this);
        var goodsid = $button.attr('goodsid');
        console.log(goodsid);
        $.getJSON('/axfmarket/addTocart/',
            {'goodsid':goodsid},
            function (data) {
                if(data['status'] == 200){
                    //prev() 上一个标签
                    console.log(data['c_goods_num']);
                    $button.prev().html(data['c_goods_num'])
                }else {
                    //跳转到登录页面
                    // alert('ss')
                    window.open('/axfuser/login/',target="_self")
                }
            }
            );
    });
    $('.subShopping').click(function () {
        var $button = $(this);
        var goodsid = $button.attr('goodsid');
        console.log(goodsid);
        $.getJSON('/axfmarket/subTocart/',
            {'goodsid':goodsid},
            function (data) {
                if(data['status'] == 200){
                    //next() 下一个标签
                    // console.log(data['c_goods_num']);
                    if(data['c_goods_num'] == 0){
                        $button.next().html(data['c_goods_num'])
                    }else {
                        $button.next().html(data['c_goods_num'])
                    }

                }else {
                    //跳转到登录页面
                    window.open('/axfuser/login/',target="_self")
                }
            }
            );
    })
});