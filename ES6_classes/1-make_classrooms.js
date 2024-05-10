export default class ClassRoom {
    constructor(maxStudentsSize) {
      this._maxStudentsSize = maxStudentsSize;
    }
  }

function initializeRooms() {
  const room1 = new ClassRoom(19);
  const room2 = new ClassRoom(20);
  const room3 = new ClassRoom(34);

  return [room1, room2, room3];
}
