import sqlite3

def get_valor(conn):
    sql = """
    with ex as (
    select * from s3000 ex
    where
    ex.infoExclusao_tpEvento = 'S-1200'),

    validos as( 
    select t.* from s5001 t
    left join ex on t.nrRecArqBase = ex.infoExclusao_nrRecEvt and ex.infoExclusao_perApur = t.perApur and ex.infoExclusao_cpfTrab = t.cpfTrab
    where ex.id is null)


    --select s.matricula, s.valor_baseInss from validos s
    --select s.matricula, SUM(s.valor_baseInss) from validos s
    --where s.perApur = '2024-01'
    --and matricula is not null

    select 
    s.perApur, 
    count(s.perApur),
    sum(s.vrCpSeg),
    sum(s.vrDescSeg),
    sum(valor_baseInss),
    sum(valor_descInss)
    from validos s 
    group by s.perApur
    """
    return conn.execute(sql)

def get_valor_analitico(conn):
    sql = """
    with ex as (
    select * from s3000 ex
    where
    ex.infoExclusao_tpEvento = 'S-1200'),

    validos as( 
    select t.* from s5001 t
    left join ex on t.nrRecArqBase = ex.infoExclusao_nrRecEvt and ex.infoExclusao_perApur = t.perApur and ex.infoExclusao_cpfTrab = t.cpfTrab
    where ex.id is null)


    --select s.matricula, s.valor_baseInss from validos s
    --select s.matricula, SUM(s.valor_baseInss) from validos s
    --where s.perApur = '2024-01'
    --and matricula is not null

    select 
    s.*
    from validos s 
    """
    return conn.execute(sql)