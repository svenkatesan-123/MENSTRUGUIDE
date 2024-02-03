const workSection = document.querySelector(".counter");

      const workSectionObserve = (entries) => {
        const [entry] = entries;
        if (!entry.isIntersecting) return;
        console.log(entries);


        const counterNum = document.querySelectorAll(".counterh2");

        const speed = 100;

        counterNum.forEach((curElem) => {

          const updateNumber = () => {
            const targetNumber = parseInt(curElem.dataset.number);
            // console.log(targetNumber);
            const initialNum = parseInt(curElem.innerText);
            // console.log(initialNum);

            const incrementNumber = Math.trunc(targetNumber / speed);
            // console.log(incrementNumber);
            if (initialNum < targetNumber) {
              curElem.innerText = `${initialNum + incrementNumber}+`;

              setTimeout(updateNumber, 10);
            } else {
              curElem.innerText = `${targetNumber}+`;
            }
          };

          updateNumber();
        });
      };
      const workSecObserver = new IntersectionObserver(workSectionObserve, {
        root: null,
        threshold: 0,
      });

      workSecObserver.observe(workSection);