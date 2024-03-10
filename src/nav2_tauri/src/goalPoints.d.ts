type Point = {
  x: number,
  y: number,
}

export const goalPoints: Map<string, Point> = new Map([
  ["start", { x: 0, y: 0 }],
  ["p1", { x: 1, y: 0 }],
  ["p2", { x: 0, y: 1 }],
  ["p3", { x: 1, y: 1 }],
  ["p4", { x: 0, y: 2 }],
]);
