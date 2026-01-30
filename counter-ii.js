/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const initVal = init;
    const increment = () => ++init;
    const decrement = () => --init;
    const reset = () => {
        init = initVal
        return init;
    };

    return {increment, decrement, reset};
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
