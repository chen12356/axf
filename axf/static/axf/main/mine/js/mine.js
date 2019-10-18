// $(function () {
//         var login_status_len = $(this).find('input[name=name]').val().length;
//         console.log(login_status_len);
//         if (login_status_len != 0 ){
//             $('#icon').css('display','none');
//             $('#new_icon').show();
//             $('#no_name').css('display','none');
//             $('#username').show();
//         }
//    $('#tologin').click(function () {
//        if (login_status_len == 0){
//          location.href = '/axfuser/login/';
//        }else {
//            // alert('')
//        }
//    })
                // $('#icon').attr('hidden','hidden');

   //              // console.log(login_status);
   //                  // $.getJSON('/axfuser/login/',
   //                  //     {'login_status':login_status},
   //                  //     function (context) {
   //                  //         console.log(context['name']);
   //                  //         console.log(context['icon']);
   //                  //     }
   //                  //     )
   //          }
   //          else {
   //              // $('#icon').attr('hidden','show');
   //              // $('#new_icon').attr('hidden','hidden');
   //              // console.log('灭比较');
   //          }
   // })
// });
$(function () {
    $('#tologin').click(function () {
        window.open('/axfuser/login/',target='_self')
    })
});