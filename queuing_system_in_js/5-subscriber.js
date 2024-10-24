import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('connect', () => {
    console.log('Redis client connected to the server');
});

redisClient.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// subscribe to channel
redisClient.subscribe('holberton school channel');

// message handling
redisClient.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        redisClient.unsubscribe('holberton school channel');
        redisClient.quit();
    } else {
        console.log(message);
    }
});