import pygame
import random

# ㅡㅡㅡㅡㅡㅡㅡ
# 1. 기본값 설정
# ㅡㅡㅡㅡㅡㅡㅡ

SCREEN_WIDTH     = 1200
SCREEN_HEIGHT    = 800
FPS              = 60
TOTAL_QUESTIONS  = 10

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
GRAY   = (180, 180, 180)
GREEN  = (50,  200, 50)
RED    = (200, 50,  50)
BEIGE  = (245, 235, 210)
BROWN  = (139, 90,  43)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 2. 유물 클래스 & 이미지 로더
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class Relic:
    def __init__(self, name, category, authentic_image=None, fake_image=None, color=None):
        self.name               = name
        self.category           = category
        self.authentic_image    = authentic_image
        self.fake_image         = fake_image
        self.color              = color

def load_image(relic, size=(350, 350), image_type="authentic"):
    image_path = relic.authentic_image if image_type == "authentic" else relic.fake_image
    try:
        img = pygame.image.load(image_path)
        img = pygame.transform.scale(img, size)
        return img
    except:
        surface = pygame.Surface(size)
        surface.fill(relic.color if relic.color else (200, 200, 200))
        return surface

def load_relics():
    return [
        Relic("주먹도끼",    "석기",   authentic_image="rockaxe(real).jpg", fake_image="rockaxe(fake).jpg"),
        Relic("빗살무늬토기", "토기",   authentic_image="peakdojagi(real).jpg", fake_image="peakdojagi(fake).jpg"),
        Relic("반달돌칼",    "석기",   authentic_image="halfmoonknife(real).jpg", fake_image="halfmoonknife(fake).jpg"),
        Relic("와질토기",    "토기",   authentic_image="bowl(real).jpg", fake_image="bowl(fake).jpg"),
        Relic("거푸집",      "금속",   authentic_image="knifecase(real).jpg", fake_image="knifecase(fake).jpg"),
        Relic("금동관",      "금속",   authentic_image="goldcrown(real).jpg", fake_image="goldcrown(fake).jpg"),
        Relic("손검",        "금속",   authentic_image="handknife(real).jpg", fake_image="handknife(fake).jpg"),
        Relic("상평통보",    "금속",   authentic_image="oldmoney(real).jpg", fake_image="oldmoney(fake).jpg"),
        Relic("고려청자",    "도자기", authentic_image="koreadojagi(real).jpg", fake_image="koreadojagi(fake).jpg"),
        Relic("가락지",      "장신구", authentic_image="okring(real).jpg", fake_image="okring(fake).jpg"),
        Relic("명패",        "장신구", authentic_image="nametag(real).jpg", fake_image="nametag(fake).jpg"),
        Relic("청화백자",    "도자기", authentic_image="bluedojagi(real).jpg", fake_image="bluedojagi(fake).jpg"),
        Relic("등잔",        "민속",   authentic_image="candlebase(real).jpg", fake_image="candlebase(fake).jpg"),
        Relic("민무늬토기",  "토기",   authentic_image="highbowl(real).jpg", fake_image="highbowl(fake).jpg"),
    ]

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 3. 메뉴 화면 클래스
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class MenuScene:
    def __init__(self, screen):
        self.screen     = screen
        self.font_title = pygame.font.SysFont("malgungothic", 55, bold=True)
        self.font_sub   = pygame.font.SysFont("malgungothic", 28)
        try:
            self.background = pygame.image.load("background.jpg")
            self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        except:
            self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self.background.fill(BEIGE)

        self.start_btn = pygame.Rect(SCREEN_WIDTH // 2 - 160, 440, 320, 75)
        self.dict_btn  = pygame.Rect(SCREEN_WIDTH // 2 - 160, 540, 320, 75)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_btn.collidepoint(event.pos):
                return "instruction"
            elif self.dict_btn.collidepoint(event.pos):
                return "dictionary"
        return "menu"

    def update(self): pass

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(100); overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        title = self.font_title.render("박물관 유물 퀴즈", True, BROWN)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 200))
        desc = self.font_sub.render("유물 이름에 맞는 이미지를 골라보세요!", True, WHITE)
        self.screen.blit(desc, (SCREEN_WIDTH // 2 - desc.get_width() // 2, 330))

        pygame.draw.rect(self.screen, BROWN, self.start_btn, border_radius=12)
        btn_text1 = self.font_sub.render("게임 시작", True, WHITE)
        self.screen.blit(btn_text1, (self.start_btn.centerx - btn_text1.get_width() // 2, self.start_btn.centery - btn_text1.get_height() // 2))

        pygame.draw.rect(self.screen, (100, 70, 40), self.dict_btn, border_radius=12)
        btn_text2 = self.font_sub.render("유물 사전", True, WHITE)
        self.screen.blit(btn_text2, (self.dict_btn.centerx - btn_text2.get_width() // 2, self.dict_btn.centery - btn_text2.get_height() // 2))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 4. 설명 및 카운트다운 화면
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class InstructionScene:
    def __init__(self, screen, relics):
        self.screen = screen
        self.relics = relics
        self.font_mid = pygame.font.SysFont("malgungothic", 35, bold=True)
        self.font_count = pygame.font.SysFont("malgungothic", 100, bold=True)
        self.start_ticks = pygame.time.get_ticks()
        self.next_scene = "instruction"

    def handle_event(self, event):
        return self.next_scene

    def update(self):
        elapsed = pygame.time.get_ticks() - self.start_ticks
        if elapsed > 6000:
            self.next_scene = "quiz"

    def draw(self):
        self.screen.fill(BEIGE)
        elapsed = (pygame.time.get_ticks() - self.start_ticks) // 1000

        if elapsed < 3:
            msg = self.font_mid.render("상단에 나오는 유물 이름을 보고", True, BROWN)
            msg2 = self.font_mid.render("두 이미지 중 '진품'을 클릭하세요!", True, BROWN)
            self.screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, 300))
            self.screen.blit(msg2, (SCREEN_WIDTH//2 - msg2.get_width()//2, 380))
        else:
            count = 6 - elapsed
            count_text = self.font_count.render(str(count), True, RED)
            self.screen.blit(count_text, (SCREEN_WIDTH//2 - count_text.get_width()//2, 320))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 5. 유물 사전 화면 클래스 (마지막 줄 중앙 정렬 수정)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class DictionaryScene:
    def __init__(self, screen, relics):
        self.screen = screen
        self.relics = relics
        self.font_title = pygame.font.SysFont("malgungothic", 40, bold=True)
        self.font_item  = pygame.font.SysFont("malgungothic", 22, bold=True)
        self.font_sub   = pygame.font.SysFont("malgungothic", 16)
        self.font_info  = pygame.font.SysFont("malgungothic", 20)
        self.font_popup = pygame.font.SysFont("malgungothic", 30, bold=True)

        self.selected_relic = None 
        self.left_img = None
        self.right_img = None
        self.cards = [] 

        # 카드 정보 가변 정렬 계산
        card_w, card_h = 220, 120
        gap_x, gap_y = 260, 160
        start_y = 160
        total_relics = len(self.relics)

        for idx, relic in enumerate(self.relics):
            col = idx % 4
            row = idx // 4

            # 현재 줄(row)에 총 몇 개의 유물이 배치되는지 계산
            # 앞 줄은 무조건 4개, 마지막 줄은 남은 개수(여기서는 14 % 4 = 2개)만큼 계산됩니다.
            if row == (total_relics // 4):
                items_in_this_row = total_relics % 4
            else:
                items_in_this_row = 4

            # 해당 줄의 유물 개수에 맞춰 시작 X 좌표(start_x)를 동적으로 변경하여 중앙 정렬
            row_width = (items_in_this_row * card_w) + ((items_in_this_row - 1) * (gap_x - card_w))
            start_x = (SCREEN_WIDTH - row_width) // 2

            x = start_x + (col * gap_x)
            y = start_y + (row * gap_y)

            rect = pygame.Rect(x, y, card_w, card_h)
            self.cards.append((rect, relic))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.selected_relic is not None:
                self.selected_relic = None
                return "dictionary"

            for rect, relic in self.cards:
                if rect.collidepoint(event.pos):
                    self.selected_relic = relic
                    self.left_img = load_image(relic, (350, 350), "authentic")
                    self.right_img = load_image(relic, (350, 350), "fake")
                    return "dictionary"

            return "menu"
        return "dictionary"

    def update(self): pass

    def draw(self):
        self.screen.fill(BEIGE)
        
        title = self.font_title.render("유물 사전", True, BROWN)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 40))
        
        info = self.font_info.render("[유물을 클릭하면 상세 이미지를 볼 수 있습니다. 빈 곳 클릭 시 종료]", True, GRAY)
        self.screen.blit(info, (SCREEN_WIDTH // 2 - info.get_width() // 2, 100))

        for rect, relic in self.cards:
            pygame.draw.rect(self.screen, WHITE, rect, border_radius=8)
            pygame.draw.rect(self.screen, BROWN, rect, 2, border_radius=8)

            name = self.font_item.render(relic.name, True, BLACK)
            cate = self.font_sub.render(f"종류: {relic.category}", True, (100, 100, 100))
            self.screen.blit(name, (rect.x + 20, rect.y + 30))
            self.screen.blit(cate, (rect.x + 20, rect.y + 70))

        if self.selected_relic is not None:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(230)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))

            p_title = self.font_popup.render(f"[{self.selected_relic.name}] 이미지 비교", True, WHITE)
            self.screen.blit(p_title, (SCREEN_WIDTH // 2 - p_title.get_width() // 2, 80))

            left_rect  = pygame.Rect(170, 220, 350, 350)
            right_rect = pygame.Rect(680, 220, 350, 350)
            
            self.screen.blit(self.left_img, left_rect)
            self.screen.blit(self.right_img, right_rect)
            pygame.draw.rect(self.screen, GREEN, left_rect, 4) 
            pygame.draw.rect(self.screen, RED, right_rect, 4)   

            lbl_real = self.font_info.render("진품 (Authentic)", True, GREEN)
            lbl_fake = self.font_info.render("가품 (Fake)", True, RED)
            lbl_back = self.font_sub.render("화면을 클릭하면 사전 목록으로 돌아갑니다.", True, GRAY)

            self.screen.blit(lbl_real, (left_rect.centerx - lbl_real.get_width() // 2, 590))
            self.screen.blit(lbl_fake, (right_rect.centerx - lbl_fake.get_width() // 2, 590))
            self.screen.blit(lbl_back, (SCREEN_WIDTH // 2 - lbl_back.get_width() // 2, 680))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 6. 퀴즈 화면 클래스
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class QuizScene:
    def __init__(self, screen, relics):
        self.screen    = screen
        self.relics    = relics
        self.font_name = pygame.font.SysFont("malgungothic", 42, bold=True)
        self.font_info = pygame.font.SysFont("malgungothic", 26)
        self.font_pause = pygame.font.SysFont("malgungothic", 50, bold=True)

        self.score          = 0
        self.index          = 0
        self.feedback       = None
        self.feedback_timer = 0
        self.next_scene     = "quiz"
        
        self.is_paused      = False 

        self.questions = random.sample(self.relics, TOTAL_QUESTIONS)
        self.load_question()

    def load_question(self):
        self.feedback = None
        self.answer   = self.questions[self.index]
        auth_img = load_image(self.answer, (350, 350), "authentic")
        fake_img = load_image(self.answer, (350, 350), "fake")

        if random.choice([True, False]):
            self.left_img, self.right_img = auth_img, fake_img
            self.correct_pos = "left"
        else:
            self.left_img, self.right_img = fake_img, auth_img
            self.correct_pos = "right"

        self.left_rect  = pygame.Rect(150, 220, 350, 350)
        self.right_rect = pygame.Rect(700, 220, 350, 350)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.is_paused:
                    return "menu"
                else:
                    self.is_paused = True
                    return "quiz"

        if self.is_paused:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_paused = False
            return self.next_scene

        if self.feedback: return self.next_scene
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.left_rect.collidepoint(event.pos):
                res = (self.correct_pos == "left")
            elif self.right_rect.collidepoint(event.pos):
                res = (self.correct_pos == "right")
            else: return "quiz"

            if res: self.score += 1
            self.feedback = "correct" if res else "wrong"
            self.feedback_timer = pygame.time.get_ticks()
        return self.next_scene

    def update(self):
        if self.is_paused: return

        if self.feedback:
            if pygame.time.get_ticks() - self.feedback_timer > 900:
                self.index += 1
                if self.index < len(self.questions): self.load_question()
                else: self.next_scene = "result"

    def draw(self):
        self.screen.fill(BEIGE)
        
        num_text = self.font_info.render(f"{self.index + 1} / {TOTAL_QUESTIONS}", True, GRAY)
        self.screen.blit(num_text, (20, 20))
        name_text = self.font_name.render(self.answer.name, True, BROWN)
        self.screen.blit(name_text, (SCREEN_WIDTH // 2 - name_text.get_width() // 2, 90))
        
        self.screen.blit(self.left_img, self.left_rect)
        self.screen.blit(self.right_img, self.right_rect)
        pygame.draw.rect(self.screen, GRAY, self.left_rect, 3)
        pygame.draw.rect(self.screen, GRAY, self.right_rect, 3)

        if self.feedback == "correct":
            target = self.left_rect if self.correct_pos == "left" else self.right_rect
            pygame.draw.rect(self.screen, GREEN, target, 10)
        elif self.feedback == "wrong":
            target = self.right_rect if self.correct_pos == "left" else self.left_rect
            pygame.draw.rect(self.screen, RED, target, 10)

        score_text = self.font_info.render(f"현재 점수: {self.score} / {TOTAL_QUESTIONS}", True, BLACK)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 680))

        if self.is_paused:
            pause_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            pause_overlay.set_alpha(200) 
            pause_overlay.fill(BLACK)
            self.screen.blit(pause_overlay, (0, 0))

            p_title = self.font_pause.render("일 시 정 지", True, WHITE)
            p_desc1 = self.font_info.render("화면을 클릭하면 게임이 다시 시작(재개)됩니다.", True, WHITE)
            p_desc2 = self.font_info.render("ESC를 한 번 더 누르면 처음 화면으로 이동합니다.", True, RED)

            self.screen.blit(p_title, (SCREEN_WIDTH//2 - p_title.get_width()//2, 300))
            self.screen.blit(p_desc1, (SCREEN_WIDTH//2 - p_desc1.get_width()//2, 420))
            self.screen.blit(p_desc2, (SCREEN_WIDTH//2 - p_desc2.get_width()//2, 480))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 7. 결과 화면 클래스
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class ResultScene:
    def __init__(self, screen, score):
        self.screen = screen; self.score = score
        self.font_title = pygame.font.SysFont("malgungothic", 50, bold=True)
        self.font_score = pygame.font.SysFont("malgungothic", 42)
        self.font_grade = pygame.font.SysFont("malgungothic", 32)

    def draw(self):
        self.screen.fill(BEIGE)
        title = self.font_title.render("Super!", True, BROWN)
        self.screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 200))
        score_t = self.font_score.render(f"최종 점수: {self.score} / {TOTAL_QUESTIONS}", True, BLACK)
        self.screen.blit(score_t, (SCREEN_WIDTH//2 - score_t.get_width()//2, 300))
        btn_text = self.font_grade.render("아무 곳이나 클릭하여 메뉴로", True, GRAY)
        self.screen.blit(btn_text, (SCREEN_WIDTH//2 - btn_text.get_width()//2, 500))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: return "menu"
        return "result"
    def update(self): pass

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 8. 씬 전환 및 실행
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def change_scene(screen, relics, next_scene, current):
    if next_scene == "menu": return MenuScene(screen)
    elif next_scene == "instruction": return InstructionScene(screen, relics)
    elif next_scene == "dictionary": return DictionaryScene(screen, relics)
    elif next_scene == "quiz": return QuizScene(screen, relics)
    elif next_scene == "result": return ResultScene(screen, current.score)

def run():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("박물관 유물 퀴즈")
    clock, relics = pygame.time.Clock(), load_relics()
    scene, current = "menu", MenuScene(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); return
            ns = current.handle_event(event)
            if ns != scene:
                scene = ns
                current = change_scene(screen, relics, ns, current)

        current.update()
        if hasattr(current, "next_scene") and current.next_scene != scene:
            scene = current.next_scene
            current = change_scene(screen, relics, scene, current)

        current.draw()
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    run()
