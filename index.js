fetch('./human.json')
    .then(response => response.json())
    .then(data => writeHTML(data))
    .catch(error => console.log(error));


function writeHTML(data) {
    elements = '';
    container = document.getElementById("object_container")

    for (var key in data) {
        fstName = data[key]['First name']
        lstName = data[key]['Last name']
        age = data[key]['Age']
        energy = data[key]['Energy']
        maxHealth = data[key]['Max Health']
        currentHealth = data[key]['Current Health']
        saludo = data[key]['Saludo']

        elements +=
            `
        <div class='col-md-6 profile_container mt-3'>
        <div class='row'>
            <div class='col-3 profile_img'>
            <img src='https://avataaars.io/?avatarStyle=Circle&topType=LongHairBob&accessoriesType=Blank&hairColor=Blonde&facialHairType=BeardLight&facialHairColor=BrownDark&clotheType=ShirtCrewNeck&clotheColor=PastelYellow&eyeType=Surprised&eyebrowType=UnibrowNatural&mouthType=Grimace&skinColor=Brown'
/>
            </div>
            <div class='col-9 profile_info'>
                <div class='row profile_header'>
                    <div class='col-6 mt-2'>
                        <h6>`+ fstName + ` ` + lstName + `</h6>
                        <h6 class=''>`+ age + ` Years Old</h6>
                    </div>
                    <div class='col-6 mt-2'>
                        <div class='progress mt-1'>
                            <div class='progress-bar bg-danger' role='progressbar' style='width: `+ currentHealth + `%'
                                aria-valuenow='100' aria-valuemin='0' aria-valuemax='100'>Health</div>
                        </div>
                        <div class='progress mt-2'>
                            <div class='progress-bar bg-warning' role='progressbar' style='width: `+ energy + `%;'
                                aria-valuenow='25' aria-valuemin='0' aria-valuemax='100'>Energy</div>
                        </div>
                    </div>

                </div>
                <div class='row'>
                    <p class='text-muted mt-2'>
                    `+ saludo + `
                    </p>
                </div>
            </div>
        </div>
    </div>`
    }




    container.innerHTML += elements
}