$(function () {
    $('.subShopping').click(function () {
        var $button = $(this);
        var $div = $button.parent().parent();
        var cartid = $div.attr('cartid');
        $.post('/axfcart/subShopping/',
                {'cartid':cartid},
                function (data) {
                if (data['status']== 200){
                    $button.next().html(data['c_goods_num']);
                }else {
                    $div.remove();
                }
                $('#menoy').html(data['total_price']);
                }

            );



    });
    $('.confirm').click(function () {
        var $confirm = $(this);
        var $div = $confirm.parent();
        var cartid = $div.attr('cartid');
        $.ajax({ url:'/axfcart/changeStatus/',
                data: {'cartid':cartid},
                type:"GET",
                dataType:'json',
                success:function (data) {
                    if (data['status']==200){
                        if (data['c_is_select']){
                            $confirm.find('span').find('span').html('✓');
                            $('#menoy').html(data['total_price']);
                        }else{
                            $confirm.find('span').find('span').html('');
                            $('#menoy').html(data['total_price']);
                        }if(data['is_all_select']){
                            //返回了true，说明此时，都被选中了，那么全选那需要打钩
                            $('.all_select').find('span').find('span').html('✓')
                        }else {
                            $('.all_select').find('span').find('span').html('')
                        }
                    }
                }
            });
    });
    $('.all_select').click(function () {
        var $div = $(this);
        alert('xxx')
        //方法一：以下思路，不建议使用，
        // var content = $div.find('span').find('span').html();
        // var data;
        // if(content){
        //     data = {'info':0}
        // }else {
        //     data = {'info':1}
        // }
        // $.ajax({
        //     url:'/axfcart/all_status/',
        //     data:data,
        //     type: 'GET',
        //     dataType: 'json',
        //     success:function (data) {
        //         if (data['status'==200]){
        //             console.log(data['c_is_select'])
        //         }
        //     }
        // });
        //方法2：定义列表，将选中和为选中的id分别放到对于列表中，传过去
    //     注意：不能直接传列表，需要join拼接成字符串
        var select_list = [];
        var unselect_list = [];
       //得到对于的商品的状态，使用标签的遍历，获取商品的id，方法each
        //找到要遍历的标签
        var $confirm = $('.confirm');
        $confirm.each(function () {
        //    获取每一个cartid,注意下面的this是指当前的对象
            var cartid = $(this).parent().attr('cartid');
            //判断当前的对象有没有被勾上，
            if($(this).find('span').find('span').html()){
            //    说明有值，把对应的id存入指定列表里
                select_list.push(cartid);
            }else {
                unselect_list.push(cartid);
            }
        });
        var unselect_len = unselect_list.length;
        var select_len = select_list.length;
        if (unselect_len== 0 && select_len==0){
        }else {
            var carid_str;
            //现在判断下列表有没有值lengh方法求长度

            if ( unselect_len > 0){
                //由于不能传送列表，那么使用join，将列表转成字符串
               carid_str = unselect_list.join('#');
            }else {
                carid_str = select_list.join('#');
            }alert(carid_str);
            $.getJSON('/axfcart/all_select/',
                {'cartid_str':carid_str},
                function (data) {
                if(unselect_len> 0){
                    $('.all_select').find('span').find('span').html('✓');
                    $('.confirm').find('span').find('span').html('✓');

                }else {
                    $('.all_select').find('span').find('span').html('');
                    $('.confirm').find('span').find('span').html('');
                }
                $('#menoy').html(data['total_price'])
                }
                )

        }

    });
    $('#btn').click(function(){
        var $btn = $(this);

        var select_list = [];
        var unselect_list = [];

        //找到要遍历的标签
        var $confirm = $('.confirm');
        $confirm.each(function () {
        //    获取每一个cartid,注意下面的this是指当前的对象
            var cartid = $(this).parent().attr('cartid');
            //判断当前的对象有没有被勾上，
            if($(this).find('span').find('span').html()){
            //    说明有值，把对应的id存入指定列表里
                select_list.push(cartid);
            }else {
                unselect_list.push(cartid);
            }
        });
        if (select_list.length == 0){
            return;
        }else {
            $.ajax({
                url:'/axforder/make_order/',
                type: 'GET',
                dataType: 'json',
                success:function (data) {
                    if (data['status']==200){
                        alert(data['order_id']);
                        window.location.href = '/axforder/order_detail/?order_id='+data['order_id']
                    }
                }
            })
        }
    });
});
