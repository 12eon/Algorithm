function solution(weight) {
    weight.sort((a, b) => a - b)
    let answer = 1
    for (const w of weight) {
        if (answer >= w)
            answer+=w
        else
            break
    }
    return answer
}

solution([3, 1, 6, 2, 7, 30, 1]);