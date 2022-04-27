const myPromise = new Promise((resolve, reject) => {
   const num = Math.floor(Math.random() * 10 + 1)
    if(num <= 7){
        resolve(num)
    } else {
        console.log(num)
        reject(new Error('Nope!'))
    }
  });
  
  myPromise
    .then(res => console.log("resolved: ", res))
    .catch(rej => console.error("rejected: ", rej))
    .finally(fin=> console.log("finally", fin))

  