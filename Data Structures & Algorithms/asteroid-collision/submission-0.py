class Solution:
    # 735 Asteroid Collision
# 只有 stack[-1] > 0 and a < 0 才会碰撞
# 栈顶小：pop，继续撞
# 一样大：pop，当前也消失
# 栈顶大：当前消失
# 当前没消失，最后 append
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            while stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a:
                    # 栈顶行星更小，被撞碎
                    stack.pop()
                    continue

                elif stack[-1] == -a:
                    # 一样大，两个都碎
                    stack.pop()
                    alive = False
                    break

                else:
                    # 栈顶行星更大，当前 a 被撞碎
                    alive = False
                    break

            if alive:
                stack.append(a)

        return stack