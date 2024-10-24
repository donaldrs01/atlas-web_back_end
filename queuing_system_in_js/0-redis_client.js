import { createClient } from 'redis';

const redisClient = createClient();

// Listen for errors before connecting to client
redisClient.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

// Establish connection to Redis server
redisClient.connect().then(() => {
    console.log('Redis client connected to the server');
});

// I installed Redis system-wide, so I need to use system-wide path when starting Redis:
// /usr/bin/redis-server > /dev/null 2>&1 &
