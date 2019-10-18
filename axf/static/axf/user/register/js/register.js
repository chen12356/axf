$(function () {
    checkName();
    checkPassword();
    checkEmail() ;
});

function checkName() {
      $('#exampleInputName').blur(function () {
       var name = $(this).val();
   //    设置正则,判断获取的name是否符合正则
       var reg  = /^[a-zA-Z]{3,6}$/;
       //正则表达式.test(变量) -->匹配成功返回true
       b = reg.test(name)
       if(b){
       //    为true此时说明前端验证成功
       //       现在进行后端验证,用户名
           $.getJSON('/axfuser/checkName/',
               //注意:数据以json的格式传输.需要用{}
               {'name':name},
               function(data){
                    if(data['status'] ==200){
                        $('#NameInfo').html(data['msg']).css({'color':'green','font-size':10})
                    }
                    else {

                        $('#NameInfo').html(data['msg']).css({'color':'red','font-size':10})
                        $(this).val('')
                    }
                    submit_disabled()
           })
       }
       else{
           $('#NameInfo').html('用户名格式错误').css({'color':'red','font-size':10})
           $(this).val('')
       }
       submit_disabled()
   })
}

function checkPassword() {
    $('#exampleInputPassword1').blur(function () {
        var password = $(this).val();
        var reg = /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,10}$/;
        b = reg.test(password);
        if (b){
            $('#pwd').html('密码格式正确').css({'color':'green','font-size':10});
        }else {
            $('#pwd').html('密码格式错误').css({'color':'red','font-size':10});
            $(this).val('')
        }
        submit_disabled()

    });
    $('#exampleInputPassword2').blur(function () {
        var comfirm_pwd = $(this).val();
        var pwd = $('#exampleInputPassword1').val();
          if (pwd == comfirm_pwd){
                $('#confirm_pwd').html('两次密码一致').css({'color':'green','font-size':10});

          } else{
                $('#confirm_pwd').html('两次密码不一致').css({'color':'red','font-size':10});
                $(this).val('')
            }submit_disabled()
    })

}
function checkEmail() {
      $('#exampleInputEmail').blur(function () {
       var email = $(this).val();
       // var reg  = /^[1-9]\d{5,10}@qq\.com$/;
       var reg  = /(?:[0-9a-zA-Z_]+.)+@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}/;
       //正则表达式.test(变量) -->匹配成功返回true
       b = reg.test(email)
       if(b) {
           $('#emailInfo').html('邮箱格式正确').css({'color': 'green', 'font-size': 10});
       }else{
           $('#emailInfo').html('邮箱格式错误').css({'color':'red','font-size':10});
           $(this).val('')
       }
       submit_disabled()
   })
}

//判断按钮是否可用
function submit_disabled() {
    var flg = true;
    var name_len = $('input[name=name]').val().length;
    var password_len = $('input[name=password]').val().length;
    var confirm_pwd_len = $('input[name=confirm_pwd]').val().length;
    var email = $('input[name=email]').val().length;
    if (name_len == 0 || password_len == 0 || confirm_pwd_len == 0 || email == 0){
        console.log('存在空')
        $('#sub').attr("disabled",flg);
    }else {
        flg = false;
        $('#sub').attr("disabled",flg);
    }
}

//前端密码加密
function parse1() {
    var password = document.getElementById("exampleInputPassword1").value;
    password = md5(password);
    document.getElementById('exampleInputPassword1').value = password;

    return true;
}