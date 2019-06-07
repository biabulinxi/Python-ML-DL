$(function () {
    $("#uname").keyup(function () {
        /*
        * 请求地址:/01-search
        * 请求方式:get
        * 请求参数:uname
        * 响应数据:["",""]
        */
        var xhr=createXhr();
        var url = "/01-search?uname="+this.value;
        xhr.open('get',url,true);
        xhr.onreadystatechange=function () {
            if (xhr.readyState==4&&xhr.status==200){
                // 1.接收收据并转换成js对象
                var arr = JSON.parse(xhr.responseText);
                // 2.判断arr中是否有元素，有则显示，没有则隐藏
                if(arr.length>0){
                    // 清空 #show 里的内容
                    $("#show").html("");
                    $("#show").css("display","blok");
                    // 循环遍历arr,将元素构建p标记，追加到show里面
                    $.each(arr,function (i,obj) {
                       var $p=$("<p>"+obj+"</p>");
                       $("#show").append($p)
                    });
                }else{
                    $("#show").css("display","none");
                }

            }
        };
        xhr.send(null)
    })
});