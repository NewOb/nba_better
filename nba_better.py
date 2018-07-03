from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

class NBA12(db.Model):
    __tablename__ = 'twelve'
    RK = db.Column(db.Integer,primary_key=True)
    Player = db.Column(db.String(255))
    Pos = db.Column(db.String(255))
    Age = db.Column(db.Integer)
    Tm = db.Column(db.String(255))
    G = db.Column(db.Integer)
    GS = db.Column(db.Integer)
    MP = db.Column(db.String(255))
    FG = db.Column(db.String(255))
    FGA = db.Column(db.String(255))
    FGlv = db.Column(db.String(255))
    ThreeP = db.Column(db.String(255))
    ThreePA = db.Column(db.String(255))
    ThreePlv = db.Column(db.String(255))
    TwoP = db.Column(db.String(255))
    TwoPA = db.Column(db.String(255))
    TwoPlv = db.Column(db.String(255))
    eFGlv = db.Column(db.String(255))
    FT = db.Column(db.String(255))
    FTA = db.Column(db.String(255))
    FTlv = db.Column(db.String(255))
    ORB = db.Column(db.String(255))
    DRB = db.Column(db.String(255))
    TRB = db.Column(db.String(255))
    AST = db.Column(db.String(255))
    STL = db.Column(db.String(255))
    BLK = db.Column(db.String(255))
    TOV = db.Column(db.String(255))
    PF = db.Column(db.String(255))
    PSG = db.Column(db.String(255))

    #test1 = NBA12.query.filter(NBA12.Tm == 'PHI').all()
    #print(test1.Player)
    #return 'index'

class NBA13(db.Model):
    __tablename__ = 'thirteen'
    RK = db.Column(db.Integer, primary_key=True)
    Player = db.Column(db.String(255))
    Pos = db.Column(db.String(255))
    Age = db.Column(db.Integer)
    Tm = db.Column(db.String(255))
    G = db.Column(db.Integer)
    GS = db.Column(db.Integer)
    MP = db.Column(db.String(255))
    FG = db.Column(db.String(255))
    FGA = db.Column(db.String(255))
    FGlv = db.Column(db.String(255))
    ThreeP = db.Column(db.String(255))
    ThreePA = db.Column(db.String(255))
    ThreePlv = db.Column(db.String(255))
    TwoP = db.Column(db.String(255))
    TwoPA = db.Column(db.String(255))
    TwoPlv = db.Column(db.String(255))
    eFGlv = db.Column(db.String(255))
    FT = db.Column(db.String(255))
    FTA = db.Column(db.String(255))
    FTlv = db.Column(db.String(255))
    ORB = db.Column(db.String(255))
    DRB = db.Column(db.String(255))
    TRB = db.Column(db.String(255))
    AST = db.Column(db.String(255))
    STL = db.Column(db.String(255))
    BLK = db.Column(db.String(255))
    TOV = db.Column(db.String(255))
    PF = db.Column(db.String(255))
    PSG = db.Column(db.String(255))

    #test1 = NBA13.query.filter(NBA13.Tm == 'PHI').first()
    #print(test1.Player)
    #return 'index'

class NBA14(db.Model):
    __tablename__ = 'fourteen'
    RK = db.Column(db.Integer, primary_key=True)
    Player = db.Column(db.String(255))
    Pos = db.Column(db.String(255))
    Age = db.Column(db.Integer)
    Tm = db.Column(db.String(255))
    G = db.Column(db.Integer)
    GS = db.Column(db.Integer)
    MP = db.Column(db.String(255))
    FG = db.Column(db.String(255))
    FGA = db.Column(db.String(255))
    FGlv = db.Column(db.String(255))
    ThreeP = db.Column(db.String(255))
    ThreePA = db.Column(db.String(255))
    ThreePlv = db.Column(db.String(255))
    TwoP = db.Column(db.String(255))
    TwoPA = db.Column(db.String(255))
    TwoPlv = db.Column(db.String(255))
    eFGlv = db.Column(db.String(255))
    FT = db.Column(db.String(255))
    FTA = db.Column(db.String(255))
    FTlv = db.Column(db.String(255))
    ORB = db.Column(db.String(255))
    DRB = db.Column(db.String(255))
    TRB = db.Column(db.String(255))
    AST = db.Column(db.String(255))
    STL = db.Column(db.String(255))
    BLK = db.Column(db.String(255))
    TOV = db.Column(db.String(255))
    PF = db.Column(db.String(255))
    PSG = db.Column(db.String(255))

    #test1 = NBA14.query.filter(NBA14.Tm == 'PHI').first()
    #print(test1.Player)
    #return 'index'

class NBA15(db.Model):
    __tablename__ = 'fifteen'
    RK = db.Column(db.Integer, primary_key=True)
    Player = db.Column(db.String(255))
    Pos = db.Column(db.String(255))
    Age = db.Column(db.Integer)
    Tm = db.Column(db.String(255))
    G = db.Column(db.Integer)
    GS = db.Column(db.Integer)
    MP = db.Column(db.String(255))
    FG = db.Column(db.String(255))
    FGA = db.Column(db.String(255))
    FGlv = db.Column(db.String(255))
    ThreeP = db.Column(db.String(255))
    ThreePA = db.Column(db.String(255))
    ThreePlv = db.Column(db.String(255))
    TwoP = db.Column(db.String(255))
    TwoPA = db.Column(db.String(255))
    TwoPlv = db.Column(db.String(255))
    eFGlv = db.Column(db.String(255))
    FT = db.Column(db.String(255))
    FTA = db.Column(db.String(255))
    FTlv = db.Column(db.String(255))
    ORB = db.Column(db.String(255))
    DRB = db.Column(db.String(255))
    TRB = db.Column(db.String(255))
    AST = db.Column(db.String(255))
    STL = db.Column(db.String(255))
    BLK = db.Column(db.String(255))
    TOV = db.Column(db.String(255))
    PF = db.Column(db.String(255))
    PSG = db.Column(db.String(255))

    #test1 = NBA15.query.filter(NBA15.Tm == 'PHI').first()
    #print(test1.Player)
    #return 'index'

class NBA16(db.Model):
    __tablename__ = 'sixteen'
    RK = db.Column(db.Integer, primary_key=True)
    Player = db.Column(db.String(255))
    Pos = db.Column(db.String(255))
    Age = db.Column(db.Integer)
    Tm = db.Column(db.String(255))
    G = db.Column(db.Integer)
    GS = db.Column(db.Integer)
    MP = db.Column(db.String(255))
    FG = db.Column(db.String(255))
    FGA = db.Column(db.String(255))
    FGlv = db.Column(db.String(255))
    ThreeP = db.Column(db.String(255))
    ThreePA = db.Column(db.String(255))
    ThreePlv = db.Column(db.String(255))
    TwoP = db.Column(db.String(255))
    TwoPA = db.Column(db.String(255))
    TwoPlv = db.Column(db.String(255))
    eFGlv = db.Column(db.String(255))
    FT = db.Column(db.String(255))
    FTA = db.Column(db.String(255))
    FTlv = db.Column(db.String(255))
    ORB = db.Column(db.String(255))
    DRB = db.Column(db.String(255))
    TRB = db.Column(db.String(255))
    AST = db.Column(db.String(255))
    STL = db.Column(db.String(255))
    BLK = db.Column(db.String(255))
    TOV = db.Column(db.String(255))
    PF = db.Column(db.String(255))
    PSG = db.Column(db.String(255))

    #was = NBA16.query.filter(NBA16.Tm == 'was').all()
    #print(was.Player)

    #test1 = NBA16.query.filter(NBA16.Tm == 'PHI').first()
    #print(test1.Player)
    #return 'index'

@app.route('/was/',methods=['GET'])
def was_player():
    was_12 = NBA12.query.filter(NBA12.Tm == 'was').all()
    was_13 = NBA13.query.filter(NBA13.Tm == 'was').all()
    was_14 = NBA14.query.filter(NBA14.Tm == 'was').all()
    was_15 = NBA15.query.filter(NBA15.Tm == 'was').all()
    was_16 = NBA16.query.filter(NBA16.Tm == 'was').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    # print(was.Player)
    while len(was_12)>0 and len(was_13)>0 and len(was_14)>0 and len(was_15)>0 and len(was_16)>0:
        a = was_12.pop()
        b = was_13.pop()
        c = was_14.pop()
        d = was_15.pop()
        e = was_16.pop()
        # i = i+1
        # print(a.Age)
        data['player']=[e.Player]
        data['age']=[e.Age]
        data['pos']=[e.Pos]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        data['g'] = [e.G]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i/e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data={}
    players = jsonify(AllData)
    return players

@app.route('/por/',methods=['GET'])
def por_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'POR').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'POR').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'POR').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'POR').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'POR').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    # print(por_12)
    while len(por_12) > 0 and len(por_13) > 0 and len(por_14) > 0 and len(por_15) > 0 and len(por_16) > 0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/atl/',methods=['GET'])
def atl_player():
    atl_12 = NBA12.query.filter(NBA12.Tm == 'ATL').all()
    atl_13 = NBA13.query.filter(NBA13.Tm == 'ATL').all()
    atl_14 = NBA14.query.filter(NBA14.Tm == 'ATL').all()
    atl_15 = NBA15.query.filter(NBA15.Tm == 'ATL').all()
    atl_16 = NBA16.query.filter(NBA16.Tm == 'ATL').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    # print(por_12)
    while len(atl_12) > 0 and len(atl_13) > 0 and len(atl_14) > 0 and len(atl_15) > 0 and len(atl_16) > 0:
        a = atl_12.pop()
        b = atl_13.pop()
        c = atl_14.pop()
        d = atl_15.pop()
        e = atl_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/bos/',methods=['GET'])
def bos_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'BOS').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'BOS').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'BOS').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'BOS').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'BOS').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/brk/',methods=['GET'])
def brk_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'BRK').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'BRK').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'BRK').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'BRK').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'BRK').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/ben/',methods=['GET'])
def ben_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'BEN').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'BEN').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'BEN').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'BEN').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'BEN').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/chi/',methods=['GET'])
def chi_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'CHI').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'CHI').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'CHI').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'CHI').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'CHI').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/cle/',methods=['GET'])
def cle_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'CLE').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'CLE').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'CLE').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'CLE').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'CLE').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/dal/',methods=['GET'])
def dal_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'dal').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'dal').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'dal').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'dal').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'dal').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/den/',methods=['GET'])
def den_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'den').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'den').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'den').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'den').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'den').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/det/',methods=['GET'])
def det_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'det').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'det').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'det').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'det').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'det').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/gsw/',methods=['GET'])
def gsw_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'GSW').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'GSW').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'GSW').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'GSW').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'GSW').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/hou/',methods=['GET'])
def hou_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'HOU').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'HOU').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'HOU').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'HOU').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'HOU').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/ind/',methods=['GET'])
def ind_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'IND').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'IND').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'IND').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'IND').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'IND').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/lac/',methods=['GET'])
def lac_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'LAC').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'LAC').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'LAC').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'LAC').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'LAC').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/lal/',methods=['GET'])
def lal_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'LAL').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'LAL').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'LAL').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'LAL').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'LAL').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/mem/',methods=['GET'])
def mem_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'MEM').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'MEM').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'MEM').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'MEM').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'MEM').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/mia/',methods=['GET'])
def mia_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'MIA').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'MIA').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'MIA').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'MIA').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'MIA').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/mil/',methods=['GET'])
def mil_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'MIL').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'MIL').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'MIL').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'MIL').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'MIL').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/min/',methods=['GET'])
def min_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'MIN').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'MIN').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'MIN').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'MIN').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'MIN').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/nop/',methods=['GET'])
def nop_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'NOP').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'NOP').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'NOP').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'NOP').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'NOP').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    while len(por_12) and len(por_13) and len(por_14) and len(por_15) and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/nyk/',methods=['GET'])
def nyk_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'NYK').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'NYK').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'NYK').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'NYK').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'NYK').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/okc/',methods=['GET'])
def okc_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'OKC').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'OKC').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'OKC').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'OKC').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'OKC').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/orl/',methods=['GET'])
def orl_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'ORL').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'ORL').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'ORL').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'ORL').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'ORL').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/phi/',methods=['GET'])
def phi_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'PHI').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'PHI').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'PHI').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'PHI').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'PHI').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/pho/',methods=['GET'])
def pho_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'PHO').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'PHO').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'PHO').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'PHO').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'PHO').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/sac/', methods=['GET'])
def sac_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'SAC').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'SAC').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'SAC').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'SAC').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'SAC').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/sas/',methods=['GET'])
def sas_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'SAS').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'SAS').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'SAS').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'SAS').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'SAS').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/tor/',methods=['GET'])
def tor_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'TOR').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'TOR').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'TOR').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'TOR').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'TOR').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/tot/',methods=['GET'])
def tot_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'TOT').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'TOT').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'TOT').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'TOT').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'TOT').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/uta/',methods=['GET'])
def uta_player():
    por_12 = NBA12.query.filter(NBA12.Tm == 'UTA').all()
    por_13 = NBA13.query.filter(NBA13.Tm == 'UTA').all()
    por_14 = NBA14.query.filter(NBA14.Tm == 'UTA').all()
    por_15 = NBA15.query.filter(NBA15.Tm == 'UTA').all()
    por_16 = NBA16.query.filter(NBA16.Tm == 'UTA').all()
    #print(was)
    data = {}
    AllData=[]
    # i = 0
    print(por_12)
    while len(por_12)>0 and len(por_13)>0 and len(por_14)>0 and len(por_15)>0 and len(por_16)>0:
        a = por_12.pop()
        b = por_13.pop()
        c = por_14.pop()
        d = por_15.pop()
        e = por_16.pop()
        # i = i+1
        print(a.Player)
        # print(a.Age)
        data['player'] = [e.Player]
        data['age'] = [e.Age]
        data['pos'] = [e.Pos]
        data['g'] = [e.G]
        data['psg_12'] = [float(a.PSG)]
        data['psg_13'] = [float(b.PSG)]
        data['psg_14'] = [float(c.PSG)]
        data['psg_15'] = [float(d.PSG)]
        data['psg_16'] = [float(e.PSG)]
        data['ast_12'] = [float(a.AST)]
        data['ast_13'] = [float(b.AST)]
        data['ast_14'] = [float(c.AST)]
        data['ast_15'] = [float(d.AST)]
        data['ast_16'] = [float(e.AST)]
        data['tov_12'] = [float(a.TOV)]
        data['tov_13'] = [float(b.TOV)]
        data['tov_14'] = [float(c.TOV)]
        data['tov_15'] = [float(d.TOV)]
        data['tov_16'] = [float(e.TOV)]
        data['trb_12'] = [float(a.TRB)]
        data['trb_13'] = [float(b.TRB)]
        data['trb_14'] = [float(c.TRB)]
        data['trb_15'] = [float(d.TRB)]
        data['trb_16'] = [float(e.TRB)]
        data['stl_12'] = [float(a.STL)]
        data['stl_13'] = [float(b.STL)]
        data['stl_14'] = [float(c.STL)]
        data['stl_15'] = [float(d.STL)]
        data['stl_16'] = [float(e.STL)]
        data['blk_12'] = [float(a.BLK)]
        data['blk_13'] = [float(b.BLK)]
        data['blk_14'] = [float(c.BLK)]
        data['blk_15'] = [float(d.BLK)]
        data['blk_16'] = [float(e.BLK)]
        data['fga_12'] = [float(a.FGA)]
        data['fga_13'] = [float(b.FGA)]
        data['fga_14'] = [float(c.FGA)]
        data['fga_15'] = [float(d.FGA)]
        data['fga_16'] = [float(e.FGA)]
        data['fg_12'] = [float(a.FG)]
        data['fg_13'] = [float(b.FG)]
        data['fg_14'] = [float(c.FG)]
        data['fg_15'] = [float(d.FG)]
        data['fg_16'] = [float(e.FG)]
        data['fta_12'] = [float(a.FTA)]
        data['fta_13'] = [float(b.FTA)]
        data['fta_14'] = [float(c.FTA)]
        data['fta_15'] = [float(d.FTA)]
        data['fta_16'] = [float(e.FTA)]
        data['ft_12'] = [float(a.FT)]
        data['ft_13'] = [float(b.FT)]
        data['ft_14'] = [float(c.FT)]
        data['ft_15'] = [float(d.FT)]
        data['ft_16'] = [float(e.FT)]
        m = float(e.PSG) + float(e.AST) + float(e.TRB) + float(e.STL) + float(e.BLK)
        v = float(e.FGA) - float(e.FG)
        p = float(e.FTA) - float(e.FT)
        i = m - v - p - float(e.TOV)
        j = i / e.G
        data['mvp'] = [j]
        # i = float(e.TOV) + float(d.TOV)
        # data['last'] = [i]
        AllData.append(data)
        data = {}
    players = jsonify(AllData)
    return players

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
