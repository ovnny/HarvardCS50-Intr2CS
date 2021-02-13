function flipOut(){
    if(document.getElementById('main').className != 'moveMain1') {
        document.getElementById('main').className = 'moveMain1';
    }
    else {
        document.getElementById('main').className = 'moveMain-reverse';
    }
};