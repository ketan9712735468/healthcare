function onpageLoad() {

    ratings = {
        samsumg: 1.5,
        nokia: 1.7,
        windows: 2.5,
        iphone: 0,
        blackberry: 4
    }
    table = document.querySelector('.table')
    totalStar = 5;
    for (rating in ratings) {
        // get keys 
        // console.log(rating);
        // get values
        // console.log(ratings[rating])
        starPercentage = (ratings[rating] / totalStar) * 100
            // console.log('percentages ' + starPercentage)
        starRounded = Math.round(starPercentage / 10) * 10 + '%';
        // console.log(starRounded);
        innerStar = table.querySelector(`.${rating} .star-inner`);
        numberRatings = table.querySelector(`.${rating} .numberRating`);

        innerStar.style.width = starRounded;
        numberRatings.innerText = ' ' + ratings[rating];

    }




}

onpageLoad()