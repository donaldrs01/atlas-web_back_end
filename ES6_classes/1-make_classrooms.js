import ClassRoom from './0-classroom';

function initializeRooms() {
  const rooms = [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
  return rooms;
}
// Export function so it can be imported elsewhere
export default initializeRooms;
