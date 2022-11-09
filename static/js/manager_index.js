        window.Promise ||
        document.write(
            '<script src="https://cdn.jsdelivr.net/npm/promise-polyfill@8/dist/polyfill.min.js"><\/script>'
        )
        window.Promise ||
        document.write(
            '<script src="https://cdn.jsdelivr.net/npm/eligrey-classlist-js-polyfill@1.2.20171210/classList.min.js"><\/script>'
        )
        window.Promise ||
        document.write(
            '<script src="https://cdn.jsdelivr.net/npm/findindex_polyfill_mdn"><\/script>'
        )
        // 로그아웃은 내가 가지고 있는 토큰만 쿠키에서 없애면 됩니다.
        function logout(){
            $.removeCookie('mytoken');
            alert('로그아웃!')
            window.location.href='/login'
        }

        function addClass(){
            var select_teacher = $('#select_teacher')[0];
            var select_teacher_name = select_teacher.options[select_teacher.selectedIndex]
            console.log(select_teacher_name)
            $.ajax({
                type:"POST",
                url:"/api/class",
                data:{class_name_give:$('#class_name').val(),teacher_name_give:select_teacher_name.text},
                success: function(response){
                    if(response['result'] === 'success'){
                        alert("클래스가 추가 되었습니다")
                    }else{
                        alert(response['msg'])
                    }
                }
            })
        }
        function changeClassSelect(){
            var classSelect = document.getElementById("select_class");

            // select element에서 선택된 option의 text가 저장된다.
            var selectText = classSelect.options[classSelect.selectedIndex].text;

            if(selectText == "반 추가하기"){
                $('#edit_class').css("display","none");
                $('#add_class').css("display","block");

            }else{
                $('#edit_class').css("display","block");
                $('#add_class').css("display","none");
                console.log(selectText);
            }
        }