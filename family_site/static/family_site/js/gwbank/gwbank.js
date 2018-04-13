
 
    // 세자리 수 콤마
    function com(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    };
    

// chae(this.value) 셀렉터 함수
$(function(){ 
  $('#s').on('change', function(){
    chae(this.value);
  });//
});//functionfunction

// 셀렉트에서 원하는 사람 데이터 출력하는 함수

function chae(name){
 
    $(document).ready(function(){
      
      $.getJSON('/api/gwbank_api', function(data){
        var jj = '<tr><th>날 자</th><th>입출금</th><th>이 름</th><th>금 액</th></tr>';  // <th></th> 가져오기
        var sum = 0;
        if(data.length>0){
          $('#k').empty();         
          //var sum = 0; 반복문안에:comma(this['gwbank_money']), 출력:comma(sum)
          // sum 함수를 역순으로 출력하는 방법을 찾지못해 숨김
          $('#k').prepend(jj); // <th></th> 삽입코드
          
            $.each(data, function(){             
              
              var z =''; // 이 위치가 중요함.
              
                if(this['gwbank_name']==name){   // name 매개변수 값이다. 
                  
                  z += '<tr>';
                  z += '<td>'+ this['gwbank_date'] + '</td>';
                  z += '<td>' + this['gwbank_income'] + '</td>';
                  z += '<td>' + this['gwbank_name'] + '</td>';
                  z += '<td>' + com(this['gwbank_money']) + '</td>';
                  z += '</tr>';  
                         
                  $("#k").append(z).css({'margin-top': '20px','margin-bottom': '80px'});
                   
                  sum += this['gwbank_money'];
                     
                };//if               
               });//each           
            };//if  
            $('#k').append('<tr><td colspan="4">' + '계 : ' + com(sum) + '원' + '</td></tr>');              
        });//getjson  
         
      });//ready     
    };//chae 
    
// 숨기기 버튼
$(function(){
  $('#kkk').on('click', function(){
    $('#k').hide();
  });
});




  