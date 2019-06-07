// ajax版本
/*
$(function () {
    $("#btnshow").click(function () {
        //创建xhr
        var xhr = createXhr();
        //创建请求
        xhr.open("get", '/02-query', true);
        // 设置回调函数
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                var users = xhr.responseText.split("|");
                var html = "";
                for (var i = 0; i < users.length; i++) {
                    var u = users[i].split('-');
                    html += "<tr>";
                    html += "<td>" + u[0] + "</td>";
                    html += "<td>" + u[1] + "</td>";
                    html += "<td>" + u[2] + "</td>";
                    html += "<td>" + u[3] + "</td>";
                    html += "</tr>"
                }
                console.log(html);
                $("#content").html(html)

            }
        };
        //发送请求
        xhr.send(null);
    })
});
*/


// jq.ajax版本
$(function () {
  $("#btnshow").click(function () {
    $.get("/02-query", function (resText) {
        var html = "";
        $.each(resText, function (i, obj) {
            html += "<tr>";
            html += "<td>" + obj.id + "</td>";
            html += "<td>" + obj.uname + "</td>";
            html += "<td>" + obj.upwd + "</td>";
            html += "<td>" + obj.uemail + "</td>";
            html += "</tr>";
        });
        console.log(html);
        $("#content").html(html)
    }, "json");
});
});



