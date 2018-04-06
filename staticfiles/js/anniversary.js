 
    $(document).ready(function(){ 
        $.getJSON('/api/anniversary_api', function(data){
            if(data.length>0){
                   
               // $('#birthday').empty();  
                var now = new Date();
                var d = now.getFullYear();
                    d += '-' + (now.getMonth() + 1) ;
                    d += '-' + now.getDate();  
                    
                $.each(data, function(){
                    var b = this['anniversary_date'];           
                                            
                        if(b==d){
                            $('#birthday').show().append(this['anniversary_name'] + "님 생일 축하합니다!") ;
                            
                        }//if
                        
                    
                });// each
            };//if
        });//getjson
    });// ready
    
