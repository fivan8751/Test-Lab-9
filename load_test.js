import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
    stages: [
        { duration: '30s', target: 10 },    // Низкая нагрузка 
        { duration: '10s', target: 50 },    // Увеличенная нагрузка 
        { duration: '10s', target: 2000 },  //Точка отказа
    ],
    thresholds: {
        http_req_failed: ['rate<0.95'],     // Допускаем 95% ошибок 
        http_req_duration: ['p(95)<5000']   // p95 < 5s
    }
};

export default function () {
    let res = http.get('https://jsonplaceholder.typicode.com/posts/1');
    
    check(res, {
        'status 200': (r) => r.status === 200,
    });
    
    sleep(1);
}
