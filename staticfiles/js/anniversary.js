 
    $(document).ready(function(){ 
        $.getJSON('/api/anniversary_api', function(data){
            if(data.length>0){
                   
               // $('#birthday').empty();  
                var now = new Date();
                var year = now.getFullYear();
                var month = (now.getMonth() + 1) ;
                var day = now.getDate();  

                if((month+"").length<2){
                    month = "0" + month;
                }// if getMonth
                
                if((day + "").length < 2){
                    day = "0" + day;
                }// if getday

                var today = year + '-' + month + '-' + day;
               
                $.each(data, function(){
                    var b = this['anniversary_date']; 
                    var c = this['anniversary_name'];  
                    var d = '<span style="font-weight: bold; font-family:바탕;">' + this['anniversary_name']  + '</span>' + "";        
                                            
                        if(b==today){
                            //$('#birthday p').show().append('<span style="font-weight: bold; font-family:'고딕', 나눔고딕, 바탕;">' + this['anniversary_name']  + '</span>' + "" + '님의 생일을 축하합니다!') ;
                            $('#birthday p').show().append( d + '님의 생일을 축하합니다!') ;
                            
                        }//if

                        if((b==today)&&(c=='어머님 생신')){                            
                            $('#birthday1').show().append( d + '을 축하드리며, 쾌유를 빕니다!'); // 다른 <div>로 대체
                            //$('#birthday1').show().replaceWith(d + '을 축하드립니다!'); ==> css가 안먹히고, bootstarp class가 안멱힌다.
                            //$('#birthday').show().replaceWith(this['anniversary_name']+'<h2>축하드립니다</h2>'); 간단한 replaceWith 사용법                           
                        }// if end

                        if((b==today)&&(c=='아버님 기일')){                           
                            $('#birthday2').show().append( d + '입니다!'); // 다른 <div>로 대체
                            //$('#birthday1').show().replaceWith(d + '을 축하드립니다!'); ==> css가 안먹히고, bootstarp class가 안멱힌다.
                            //$('#birthday').show().replaceWith(this['anniversary_name']+'<h2>축하드립니다</h2>'); 간단한 replaceWith 사용법                           
                        }// if end
                        
                    
                });// each
            };//if
        });//getjson
    });// ready

    