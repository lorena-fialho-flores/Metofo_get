# Lorena Fialho Flores - RA:942421259


from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()

UCs = {

    1: {
        "Titulo": "Métodos, Modelos e Técnicas de Engenharia de Software",
        "Aulas": 200,
        "Horas": 168
    },

    2:{
         "Titulo": "Inteligência Artifical e Visão Computacional",
        "Aulas": 300,
        "Horas": 200

    },
     3:{
         "Titulo": "Estutura de Dados II",
        "Aulas": 300,
        "Horas": 200

    }
}

@router.get('/ucs')
async def get_ucs():
    return UCs

@router.get('/ucs/{uc_id}')
async def get_uc(uc_id: int):
    uc = UCs.get(uc_id)
    
    if not uc:
        raise HTTPException(status_code=404, detail="UC não encontrada.")
    
    uc.update({"id": uc_id})

    return uc