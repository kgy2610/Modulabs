// 동기적으로 동작하는 코드
// console.log("hello");
// console.log("world");

// 비동기적으로 동작하는 코드
// setTimeout(()=>{
//     console.log("hello");
// }, 1000);
// console.log("world");

// setTimeout(()=>{
//     console.log("hello");
// }, 0);

// console.log("world");

// 콜 스택 처리과정
const 참깨빵 = () => {
    console.log("Call 참깨빵");
    순쇠고기패티();
    console.log("End 참깨빵")
}

const 순쇠고기패티 = () => {
    console.log("Call 순쇠고기패티");
    특별한소스();
    console.log("End 순쇠고기패티");
}

const 특별한소스 = () => {
    console.log("Call 특별한소스");
    console.log("End 특별한소스");
}

참깨빵();
console.log("---- 함수 호출 종료 ----");

// ------------------ 예제 ------------------
/*
문제1: 타이머 3개 비교하기,
다음 코드를 실행하면 어떤 순서로 출력될까요?
console.log("시작");
setTimeout(() => console.log("타이머 A"), 100);
setTimeout(() => console.log("타이머 B"), 50);
console.log("중간");
setTimeout(() => console.log("타이머 C"), 0);
console.log("끝");

답 : 시작 - 중간 - 끝 - 타이머C - 타이머B - 타이머A */

/* 문제2: 직접 구현하기,
다음과 같은 순서로 출력되도록 코드를 완성하세요.

원하는 출력:
준비
시작
첫번째 작업 완료
두번째 작업 완료
모든 작업 끝
*/

// console.log("준비");

// setTimeout(() => {
//     console.log("첫번째 작업 완료");
// }, 0);

// console.log("시작");

// setTimeout(() => {
//     console.log("두번째 작업 완료");
// }, 1000);

// setTimeout(() => {
//     console.log("모든 작업 끝");
// }, 1000);

/*
문제3: 함수 + setTimeout 조합,
다음 코드의 실행 순서를 예측해보세요.

function 작업A() {
    console.log("작업A 시작");
    setTimeout(() => {
        console.log("작업A 완료");
    }, 150);
}

function 작업B() {
    console.log("작업B 시작");
    setTimeout(() => {
        console.log("작업B 완료");
    }, 100);
}

console.log("프로그램 시작");
작업A();
작업B();
console.log("프로그램 끝");

답 : 프로그램 시작 - 작업A 시작 - 작업B 시작 - 프로그램 끝 - 작업B 완료 - 작업A 완료
*/

// 비동기 제어
// const user = {};

// setTimeout(() => {
//     user.name = "weniv";
// }, 0);

// console.log(user);

// 콜백함수
// const user = {};

// function setUser(callback) {
//     setTimeout(() => {
//         user.name = "weniv";
//         callback(user);
//     }, 0);
// }

// function printUser(user) {
//     console.log(user);
// }

// setUser(printUser);
// setUser((user) => console.log(user));

// function setUSer(callback) {
//     setTimeout(() => {
//         user.name = "weniv";
//         user.age = 20;
//         callback(user);
//     }, 0);
// }

// function roleCheck(user, callback) {
//     setTimeout(() => {
//         if (user.age >= 20) {
//             user.role = "성인";
//         } else {
//             user.role = "학생";
//         }
//         callback(user);
//     }, 1000);
// }

// setUSer((user) => roleCheck(user, printUser));

// 콜백 지옥
// func1(function(result1){
//     func2(result1, function(result2){
//         func3(result2, function(result3){
//             // 계속되는 중첩...
//         });
//     });
// });

// 예제
/* 
음식 주문부터 배달까지의 과정을 콜백 함수로 구현하세요.

요구사항

1단계: 기본 주문 처리

주문접수(음식명, 고객명, 콜백함수) 함수 구현
1초 후 "주문이 접수되었습니다" 메시지 출력
완료 후 콜백 함수 실행

2단계: 음식 준비

음식준비(음식명, 콜백함수) 함수 구현
2초 소요, 준비 완료 메시지 출력
완료 후 콜백 함수 실행

3단계: 배달 시작

배달시작(음식명, 주소, 콜백함수) 함수 구현
3초 소요, 배달 완료 메시지 출력
완료 후 콜백 함수 실행

4단계: 전체 과정 연결

위 3단계를 순서대로 실행하는 코드 작성
"피자", "홍길동", "서울시 강남구"로 테스트
마지막에 "배달 완료!" 메시지 출력
*/
// function order(food, name, callback){
//     setTimeout(() => {
//         console.log(`${food} 주문이 접수되었습니다.`);
//         callback()
//     }, 1000);
// };

// function ready(food, callback){
//     setTimeout(() => {
//         console.log(`${food} 준비가 완료되었습니다.`);
//         callback()
//     });
// };

// function deli(food, address, callback){
//     setTimeout(() => {
//         console.log(`${address}로 배달을 시작합니다.`);
//         callback();
//     }, 3000);
// }

// order("피자", "홍길동", function(){
//     ready("피자", function(){
//         deli("피자", "서울시 강남구", function(){
//             console.log("배달이 완료되었습니다.")
//             console.log("배달 완료!");
//         });
//     });
// });

// ---------------------------- callback -> promise ----------------------------
// const user = {};

// function setUser() {
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             user.name = "weniv";
//             user.age = 20;
//             resolve(user);
//         }, 0);
//     });
// }

// function printUser(user) {
//     console.log(user);
// }

// function roleCheck(user) {
//     return new Promise((resolve) => {
//         setTimeout(() => {
//             if (user.age >= 20) {
//                 user.role = "성인";
//             } else {
//                 user.role = "학생";
//             }
//             resolve(user);
//         }, 1000);
//     });
// }

function setUserPromise(){
    return new Promise((resolve) => {
        setTimeout(() => {
            const user = {
                name: "weniv",
                age: 20
            };
            resolve(user);
        }, 0);
    });
}

function roleCheckPromise(user){
    return new Promise((resolve) => {
        setTimeout(() => {
            if(user.age >= 20){
                user.role = "성인";
            } else{
                user.role = "학생";
            }
            resolve(user);
        }, 1000);
    });
}

function printUser(user){
    console.log(user);
}

setUserPromise()
    .then((user) => roleCheckPromise(user))
    .then((user) => printUser(user));