function deleteSelect(selectId) {   // takes the selection id that we pass
    fetch('/delete-select', {       // sends a POST request to the /delete-select endpoint defined in the views.py file
        method: 'POST',
        body: JSON.stringify({ selectId: selectId }) //turns selectid into a string
    }).then((_res) => {             // when it gets a response, it will reload the  window
        window.location.href = "/selection";
    }) 
}