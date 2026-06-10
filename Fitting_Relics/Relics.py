# 이 유물의 이름은 무엇일까??
# 이름에 맞는 유물 맞추기 게임 !


import pygame
import random

# ㅡㅡㅡㅡㅡㅡㅡ
# 1. 기본값 설정
# ㅡㅡㅡㅡㅡㅡㅡ

SCREEN_WIDTH     = 800
SCREEN_HEIGHT    = 600
FPS              = 60
TOTAL_QUESTIONS  = 10

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
GRAY   = (180, 180, 180)
GREEN  = (50,  200, 50)
RED    = (200, 50,  50)
BEIGE  = (245, 235, 210)
BROWN  = (139, 90,  43)

BOX_COLORS = [
    (210, 180, 140),
    (188, 143, 143),
    (143, 188, 143),
    (143, 163, 188),
    (188, 170, 143),
]


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 2. 유물 클래스  ← load_image 메서드 삭제
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class Relic:        # 유물별로 
    def __init__(self, name, category, authentic_image = None, fake_image = None, color = None):
        self.name               = name
        self.category           = category
        self.authentic_image    = authentic_image  # 진품 이미지
        self.fake_image         = fake_image       # 가품 이미지
        self.color              = color

    def load_image(self, size=(250, 250), image_type="authentic"):
        image_path = self.authentic_image if image_type == "authentic" else self.fake_image
        if image_path:
            img = pygame.image.load(image_path)
            img = pygame.transform.scale(img, size)
            return img
        else:
            surface = pygame.Surface(size)
            surface.fill(self.color)
            return surface

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 3. 이미지 로딩 함수  ← 새로 추가
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def load_image(relic, size=(250, 250), image_type="authentic"):
    image_path = relic.authentic_image if image_type == "authentic" else relic.fake_image
    if image_path:
        img = pygame.image.load(image_path)
        img = pygame.transform.scale(img, size)
        return img
    else:
        surface = pygame.Surface(size)
        surface.fill(relic.color)
        return surface


# ㅡㅡㅡㅡㅡㅡㅡ
# 4. 유물 목록
# ㅡㅡㅡㅡㅡㅡㅡ

def load_relics():
    relics = [
        # 구석기
        Relic("주먹도끼",    "석기",   authentic_image="rockaxe(real).jpg", fake_image="rockaxe(fake).jpg"),
        # 신석기 / 청동기
        Relic("빗살무늬토기", "토기",   authentic_image="peakdojagi(real).jpg", fake_image="peakdojagi(fake).jpg"),
        Relic("반달돌칼",    "석기",   authentic_image="halfmoonknife(real).jpg", fake_image="halfmoonknife(fake).jpg"),
        # 원삼국
        Relic("와질토기",    "토기",   authentic_image="bowl(real).jpg", fake_image="bowl(fake).jpg"),
        Relic("거푸집",      "금속",   authentic_image="knifecase(real).jpg", fake_image="knifecase(fake).jpg"),
        # 가야
        Relic("금동관",      "금속",   authentic_image="goldcrown(real).jpg", fake_image="goldcrown(fake).jpg"),
        Relic("손검",   "금속",   authentic_image="handknife(real).jpg", fake_image="handknife(fake).jpg"),
        Relic("상평통보",   "금속",   authentic_image="oldmoney(real).jpg", fake_image="oldmoney(fake).jpg"),
        # 고려 / 조선
        Relic("고려청자",    "도자기", authentic_image="koreadojagi(real).jpg", fake_image="koreadojagi(fake).jpg"),
        Relic("가락지",    "장신구", authentic_image="okring(real).jpg", fake_image="okring(fake).jpg"),
        Relic("명패",        "장신구", authentic_image="nametag(real).jpg", fake_image="nametag(fake).jpg"),
        Relic("청화백자",    "도자기", authentic_image="bluedojagi(real).jpg", fake_image="bluedojagi(fake).jpg"),
        # 민속
        Relic("등잔",        "민속",   authentic_image="candlebase(real).jpg", fake_image="candlebase(fake).jpg"),
        Relic("민무늬토기",    "토기",   authentic_image="highbowl(real).jpg", fake_image="highbowl(fake).jpg"),
        ]
    return relics


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 5. 메뉴 화면 클래스
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class MenuScene:
    def __init__(self, screen):
        self.screen     = screen
        self.font_title = pygame.font.SysFont("malgungothic", 55, bold=True)
        self.font_sub   = pygame.font.SysFont("malgungothic", 28)
        self.font_hint  = pygame.font.SysFont("malgungothic", 22)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return "quiz"
        return "menu"

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BEIGE)

        title = self.font_title.render("박물관 유물 퀴즈", True, BROWN)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 170))

        desc = self.font_sub.render("유물 이름에 맞는 이미지를 골라보세요!", True, BLACK)
        self.screen.blit(desc, (SCREEN_WIDTH // 2 - desc.get_width() // 2, 260))

        btn_rect = pygame.Rect(SCREEN_WIDTH // 2 - 120, 350, 240, 60)
        pygame.draw.rect(self.screen, BROWN, btn_rect, border_radius=12)
        btn_text = self.font_sub.render("게임 시작", True, WHITE)
        self.screen.blit(btn_text, (
            btn_rect.centerx - btn_text.get_width() // 2,
            btn_rect.centery - btn_text.get_height() // 2
        ))

        hint = self.font_hint.render("아무 곳이나 클릭하세요", True, GRAY)
        self.screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, 470))


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 6. 퀴즈 화면 클래스
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class QuizScene:
    def __init__(self, screen, relics):
        self.screen    = screen
        self.relics = relics
        self.font_name = pygame.font.SysFont("malgungothic", 42, bold=True)
        self.font_info = pygame.font.SysFont("malgungothic", 26)
        self.font_fb   = pygame.font.SysFont("malgungothic", 36, bold=True)

        self.score          = 0
        self.index          = 0
        self.feedback       = None
        self.feedback_timer = 0
        self.next_scene     = "quiz"

        self.questions = random.sample(self.relics, TOTAL_QUESTIONS)
        self.load_question()

    def load_question(self):
        self.feedback = None
        self.answer   = self.questions[self.index]  # 정답 유물

        # 진품과 가품 이미지 로드
        authentic_img = load_image(self.answer, (250, 250), image_type="authentic")   # 진품
        fake_img      = load_image(self.answer, (250, 250), image_type="fake")        # 가품

        # 좌우 위치를 무작위로 결정
        if random.choice([True, False]):
            self.left_img  = authentic_img
            self.right_img = fake_img
            self.correct_position = "left"      # 진품이 왼쪽
        else:
            self.left_img  = fake_img
            self.right_img = authentic_img
            self.correct_position = "right"     # 진품이 오른쪽

        self.left_rect  = pygame.Rect(80,  180, 250, 250)
        self.right_rect = pygame.Rect(470, 180, 250, 250)

    def check_answer(self, selected_position):
        # selected_position: "left" 또는 "right"
        return selected_position == self.correct_position

    def draw_feedback(self):
        if self.feedback == "correct":
            if self.correct_position == "left":
                pygame.draw.rect(self.screen, GREEN, self.left_rect, 6)
            else:
                pygame.draw.rect(self.screen, GREEN, self.right_rect, 6)
            text = self.font_fb.render("정답!", True, GREEN)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 460))

        elif self.feedback == "wrong":
            if self.correct_position == "left":
                pygame.draw.rect(self.screen, RED, self.right_rect, 6)
            else:
                pygame.draw.rect(self.screen, RED, self.left_rect, 6)
            text = self.font_fb.render("오답!", True, RED)
            self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 460))

    def handle_event(self, event):
        if self.feedback is not None:
            return self.next_scene

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.left_rect.collidepoint(event.pos):
                result = self.check_answer("left")
            elif self.right_rect.collidepoint(event.pos):
                result = self.check_answer("right")
            else:
                return "quiz"

            if result:
                self.score += 1
            self.feedback       = "correct" if result else "wrong"
            self.feedback_timer = pygame.time.get_ticks()

        return self.next_scene

    def update(self):
        if self.feedback is not None:
            elapsed = pygame.time.get_ticks() - self.feedback_timer
            if elapsed > 900:
                self.index += 1
                if self.index < len(self.questions):
                    self.load_question()
                else:
                    self.next_scene = "result"

    def draw(self):
        self.screen.fill(BEIGE)

        num_text = self.font_info.render(f"{self.index + 1} / {TOTAL_QUESTIONS}", True, GRAY)
        self.screen.blit(num_text, (20, 20))

        name_text = self.font_name.render(self.answer.name, True, BROWN)
        self.screen.blit(name_text, (SCREEN_WIDTH // 2 - name_text.get_width() // 2, 90))

        hint = self.font_info.render("어느 것이 진품일까요?", True, GRAY)
        self.screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, 148))

        self.screen.blit(self.left_img,  (self.left_rect.x,  self.left_rect.y))
        self.screen.blit(self.right_img, (self.right_rect.x, self.right_rect.y))

        pygame.draw.rect(self.screen, GRAY, self.left_rect,  3)
        pygame.draw.rect(self.screen, GRAY, self.right_rect, 3)

        self.draw_feedback()

        score_text = self.font_info.render(f"점수: {self.score} / {TOTAL_QUESTIONS}", True, BLACK)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 530))


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 7. 결과 화면 클래스
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class ResultScene:
    def __init__(self, screen, score):
        self.screen     = screen
        self.score      = score
        self.font_title = pygame.font.SysFont("malgungothic", 50, bold=True)
        self.font_score = pygame.font.SysFont("malgungothic", 42)
        self.font_grade = pygame.font.SysFont("malgungothic", 32)
        self.font_hint  = pygame.font.SysFont("malgungothic", 22)

    def get_grade(self):
        ratio = self.score / TOTAL_QUESTIONS
        if ratio == 1.0:
            return "완벽해요! 박물관 전문가!"
        elif ratio >= 0.8:
            return "훌륭해요! 거의 다 맞았어요!"
        elif ratio >= 0.6:
            return "잘했어요! 조금만 더 공부해봐요."
        elif ratio >= 0.4:
            return "아쉬워요. 다시 도전해봐요!"
        else:
            return "유물 공부가 필요해요!"

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return "menu"
        return "result"

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BEIGE)

        title = self.font_title.render("게임 종료!", True, BROWN)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 130))

        score_text = self.font_score.render(f"최종 점수: {self.score} / {TOTAL_QUESTIONS}", True, BLACK)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 220))

        grade = self.font_grade.render(self.get_grade(), True, BROWN)
        self.screen.blit(grade, (SCREEN_WIDTH // 2 - grade.get_width() // 2, 300))

        btn_rect = pygame.Rect(SCREEN_WIDTH // 2 - 120, 390, 240, 60)
        pygame.draw.rect(self.screen, BROWN, btn_rect, border_radius=12)
        btn_text = self.font_grade.render("다시 하기", True, WHITE)
        self.screen.blit(btn_text, (
            btn_rect.centerx - btn_text.get_width() // 2,
            btn_rect.centery - btn_text.get_height() // 2
        ))

        hint = self.font_hint.render("아무 곳이나 클릭하세요", True, GRAY)
        self.screen.blit(hint, (SCREEN_WIDTH // 2 - hint.get_width() // 2, 490))


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 8. 씬 전환 함수 & 게임 루프
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def change_scene(screen, relics, next_scene, current):
    if next_scene == "menu":
        return MenuScene(screen)
    elif next_scene == "quiz":
        return QuizScene(screen, relics)
    elif next_scene == "result":
        return ResultScene(screen, current.score)


def run():
    pygame.init()
    screen    = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("박물관 유물 퀴즈")
    clock     = pygame.time.Clock()
    relics = load_relics()

    scene   = "menu"
    current = MenuScene(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            next_scene = current.handle_event(event)
            if next_scene != scene:
                scene   = next_scene
                current = change_scene(screen, relics, next_scene, current)

        current.update()

        if hasattr(current, "next_scene") and current.next_scene != scene:
            scene   = current.next_scene
            current = change_scene(screen, relics, scene, current)

        current.draw()
        pygame.display.flip()
        clock.tick(FPS)


# ㅡㅡㅡㅡㅡㅡㅡㅡ
# 9. 실행 진입점
# ㅡㅡㅡㅡㅡㅡㅡㅡ

if __name__ == "__main__":
    run()