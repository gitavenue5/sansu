// 세자리 수 콤마
function comma(num){
    var len, point, str;
    num = num + "";
    point = num.length % 3 ;
    len = num.length;
    str = num.substring(0, point);
    while (point < len) {
        if (str != "") str += ",";
        str += num.substring(point, point + 3);
        point += 3;
    }
    return str;
}

// 글 내용 감추기
function hidden(){  
    $(document).ready(function(){      
      $('#kkk').click(function(){
        $('#k').css({'display': 'none'});
      })//click          
    });//ready function end
}//hidden function end


// 셀렉트에서 원하는 사람 데이터 출력하는 함수
function chae(name){
    $(document).ready(function(){
     
      $.getJSON('/api/gwbank_api', function(data){
        if(data.length>0){
          $('#k').empty();
          //var sum = 0; 반복문안에:comma(this['gwbank_money']), 출력:comma(sum)
          // sum 함수를 역순으로 출력하는 방법을 찾지못해 숨김
            $.each(data, function(){
              var z = '<li>'+ this['gwbank_date'] + '</li><li>' + this['gwbank_income'] 
              + '</li><li>' + this['gwbank_name'] + '</li><li>' + comma(this['gwbank_money']) + '</li>';
             
                if(this['gwbank_name']==name){                
                    $('#k').append('<p><ul>' + z +'</ul></p>').css({'margin': '20px'});        
                      
                }//if               
            })//each
            }//if 
        })//getjson
      })//ready
    }//chae 