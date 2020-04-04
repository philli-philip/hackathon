<template>
    <div class="card">
        <div class="header">
            <span class="small">Updated 7 minutes ago</span>
            <button class="close">X</button>
        </div>
        <h3 class="title">Universätsspital Zürich</h3>
        <div class="icu-box" style="display:inline-block;">
            <span class="icu-title">ICU Low Care</span>
            <span class="icu-label greenish">
                <span class="icu-amount">400</span>
                available
            </span>
        </div>
        <div class="icu-box" style="display:inline-block;">
            <span class="icu-title">ICU High Care</span>
            <span class="icu-label redish">
            <span class="icu-amount">25</span>
            available</span>
        </div>
        <div class="icu-box">
            <span class="icu-title" >Development</span>
            <div class="bar" > </div>
            <div class="bar" > </div>
            <div class="bar" > </div>
            <div class="bar" > </div>
            <div class="bar" > </div>
            <div class="bar" > </div>
        </div>
        <div class="icu-box">
            <span class="icu-title" >Contact information</span>
            <span class="medium">Rämistrasse 100, 8091 Zürich</span>
            <span class="medium">+41 61 000 00 00</span>
        </div>
    </div>
</template>

<style scoped>
 .card {
     background-color: #fff;
     border-radius: 8px;
     box-shadow: 0px 2px 14px rgba(0, 0, 0, 0.1);
     display: block;
     position: absolute;
     bottom: 48px;
     right: 48px;
     z-index: 2000;
     padding: 0px 8px 24px 24px;
 }

.header{
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    align-items:flex-end;
}

.close{
    float: right;
    padding: 1rem;
}

 .small{
     color: #9FA2B4;
     font-size: 14px;
 }

 .title{
     font-size: 20px;
     display: block;
 }

.icu-box{
    display: block;
    margin-top: 32px;
    margin-right: 24px;
    position: relative;
}

 .icu-title{
     font-size: 14px;
     display: block;
     font-weight: 600;
     margin-bottom: 4px;
 }

 .icu-label{
     border-radius: 16px;
     line-height: 24px;
     font-size: 14px;
     font-weight: 800;
     padding: 2px 8px 3px 0px;
 }

 .icu-amount{
     color: #fff;
     border-radius: 16px;
     width: 40px;
     display: inline-block;
     text-align: center;
     font-size: 12px;
     font-weight: 600;
     line-height: 24px;
 }
.greenish.icu-label{
     background: #CAECBB;
}

.greenish .icu-amount{
     background: #59A535;
}

.redish.icu-label{
     background: #ECC3BB;
}

.redish .icu-amount{
     background: #CB5F4B;
}

.medium{
    display: block;
}
.bar{
    width: 8px;
    background-color: #CAECBB;
    height: 120px;
    position: relative;
    top: 0px;
    left: 0px;
    display: inline-block;
    margin-right: 16px;
    border-radius: 4px;
}
.bar::after{
    content: "";
    position: absolute;
    width: 8px;
    height: 16px;
    bottom: 0px;
    border-radius: 4px;
    background-color: #CB5F4B;
}
</style>
