// 通过 post 请求 发送给 //01-register
$(function () {
    $("#btnRegister").click(function () {
        var params = {
            "uname": $("#uname").val(),
            "upwd": $("#upwd").val(),
            "uemail": $("#uemail").val()
        };
        // $.ajax()
        $.ajax({
            "url":"/01-register",
            "type":"post",
            "data":params,
            "async":true,
            "success":function (data) {
                // data 表示响应回来的数据
                alert(data);
            },
            "error":function () {
                alert("程序内部错误！")
            }
        });
    })
});