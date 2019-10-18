$(function () {
    checkLogin();
});
function checkLogin() {
      $('#Name').blur(function () {
          submit_disabled();
      });
    $("#Password").blur(function () {
         submit_disabled();
    });
    $('#img_code').blur(function () {
         submit_disabled();
    })
}
//判断按钮是否可用
function submit_disabled() {
    var flg = true;
    var name_len = $('input[name=name]').val().length;
    var password_len = $('input[name=password]').val().length;
    var imgCode_len = $('input[name=imgCode]').val().length;

    if (name_len == 0 || password_len == 0 || imgCode_len==0){
        $('#sub').attr("disabled",flg);
    }else {
        flg = false;
        $('#sub').attr("disabled",flg);
    }
}

function chageImage() {
    var i = document.getElementById("changeImage");
    //获取img标签的dom对象,可以使用src方法发起请求
    i.src = '/axfuser/get_code/?'+Math.random();
}

function parse() {
    var password =  document.getElementById('Password').value;
    //使用md5加密,进行前端加密,防止在本地的cookie密码明文.这只对不懂it的来说
    password = md5(password);
    document.getElementById("Password").value = password ;
    //如果返回的为false,那么点击提交表单的内容并不会提交.
    return true;
}