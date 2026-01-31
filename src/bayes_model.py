import math
import os
from typing import Dict, List

import pandas as pd
from sqlalchemy import create_engine

try:
    from dotenv import load_dotenv
except Exception:
    try:
        from dotenv.main import load_dotenv
    except Exception as exc:
        raise RuntimeError(
            "No se encontró load_dotenv. Instala 'python-dotenv' y desinstala el paquete 'dotenv' si existe."
        ) from exc

load_dotenv()

FEATURES: List[str] = [
    'Humor', 'Culpa', 'Suicidio', 'IPrecoz', 'IIntermedio', 'ITardio', 'Trabajo',
    'Inhibicion', 'Agitacion', 'APsiquica', 'ASomatica', 'SGastrointestinales',
    'SGenerales', 'SGenitales', 'Hipocondria', 'Peso', 'Introspeccion',
    'AnimoAnsioso', 'Tension', 'Temores', 'Insomnio', 'Intelectual',
    'AnimoDeprimido', 'SomaticosMusculares', 'SomaticosSensoriales',
    'Cardiovasculares', 'Respiratorios', 'Gastrointestinales', 'Genitourinarios',
    'Autonomos'
]
CLASSES = ['Depresion', 'Ansiedad']
VALUES = ['0', '1', '2', '3', '4']

_ENGINE = None
_MODEL = None


def _get_engine():
    global _ENGINE
    if _ENGINE is None:
        db_user = os.getenv('DB_USER', 'root')
        db_password = os.getenv('DB_PASSWORD', '')
        db_host = os.getenv('DB_HOST', 'localhost')
        db_port = os.getenv('DB_PORT', '3306')
        db_name = os.getenv('DB_NAME', 'escalahamilton')
        string_connection = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        _ENGINE = create_engine(
            string_connection,
            pool_pre_ping=True,
            pool_recycle=1800
        )
    return _ENGINE


def _build_model() -> Dict[str, object]:
    engine = _get_engine()
    datos = pd.read_sql_query('SELECT * FROM conocimiento', engine)
    if datos.empty:
        return {
            'total': 0,
            'class_counts': {cls: 0 for cls in CLASSES},
            'feature_counts': {feature: pd.DataFrame(0, index=CLASSES, columns=VALUES) for feature in FEATURES},
            'values': VALUES
        }

    datos = datos.copy()
    datos['Clase'] = datos['Clase'].astype(str)
    for feature in FEATURES:
        if feature in datos.columns:
            datos[feature] = datos[feature].astype(str)

    class_counts = datos['Clase'].value_counts().to_dict()
    feature_counts = {}
    for feature in FEATURES:
        if feature not in datos.columns:
            feature_counts[feature] = pd.DataFrame(0, index=CLASSES, columns=VALUES)
            continue
        table = pd.crosstab(datos['Clase'], datos[feature])
        table = table.reindex(index=CLASSES, columns=VALUES, fill_value=0)
        feature_counts[feature] = table

    return {
        'total': len(datos),
        'class_counts': class_counts,
        'feature_counts': feature_counts,
        'values': VALUES
    }


def get_model(force_refresh: bool = False) -> Dict[str, object]:
    global _MODEL
    if _MODEL is None or force_refresh:
        _MODEL = _build_model()
    return _MODEL


def refresh_model() -> None:
    get_model(force_refresh=True)


def _prior_prob(model: Dict[str, object], cls: str) -> float:
    total = int(model['total'])
    class_counts = model['class_counts']
    return (int(class_counts.get(cls, 0)) + 1) / (total + len(CLASSES)) if total >= 0 else 0


def _conditional_prob(model: Dict[str, object], feature: str, value: str, cls: str) -> float:
    value_str = str(value) if value is not None else None
    if value_str not in model['values']:
        return 1 / len(model['values'])
    table = model['feature_counts'][feature]
    count = int(table.loc[cls, value_str]) if cls in table.index else 0
    total = int(model['class_counts'].get(cls, 0))
    k = len(model['values'])
    return (count + 1) / (total + k)


def _calculate_class_prob(cls: str, inputs: List[str]) -> float:
    model = get_model()
    probs = [
        _conditional_prob(model, feature, value, cls)
        for feature, value in zip(FEATURES, inputs)
    ]
    return _prior_prob(model, cls) * math.prod(probs)


def clase_Depresion(Humor, Culpa, Suicidio, IPrecoz, IIntermedio, ITardio, Trabajo, Inhibicion, Agitacion,
                   APsiquica, ASomatica, SGastrointestinales, SGenerales, SGenitales, Hipocondria, Peso,
                   Introspeccion, AnimoAnsioso, Tension, Temores, Insomnio, Intelectual, AnimoDeprimido,
                   SomaticosMusculares, SomaticosSensoriales, Cardiovasculares, Respiratorios, Gastrointestinales,
                   Genitourinarios, Autonomos):
    inputs = [
        Humor, Culpa, Suicidio, IPrecoz, IIntermedio, ITardio, Trabajo, Inhibicion, Agitacion, APsiquica,
        ASomatica, SGastrointestinales, SGenerales, SGenitales, Hipocondria, Peso, Introspeccion, AnimoAnsioso,
        Tension, Temores, Insomnio, Intelectual, AnimoDeprimido, SomaticosMusculares, SomaticosSensoriales,
        Cardiovasculares, Respiratorios, Gastrointestinales, Genitourinarios, Autonomos
    ]
    return _calculate_class_prob('Depresion', inputs)


def clase_Ansiedad(Humor, Culpa, Suicidio, IPrecoz, IIntermedio, ITardio, Trabajo, Inhibicion, Agitacion,
                  APsiquica, ASomatica, SGastrointestinales, SGenerales, SGenitales, Hipocondria, Peso,
                  Introspeccion, AnimoAnsioso, Tension, Temores, Insomnio, Intelectual, AnimoDeprimido,
                  SomaticosMusculares, SomaticosSensoriales, Cardiovasculares, Respiratorios, Gastrointestinales,
                  Genitourinarios, Autonomos):
    inputs = [
        Humor, Culpa, Suicidio, IPrecoz, IIntermedio, ITardio, Trabajo, Inhibicion, Agitacion, APsiquica,
        ASomatica, SGastrointestinales, SGenerales, SGenitales, Hipocondria, Peso, Introspeccion, AnimoAnsioso,
        Tension, Temores, Insomnio, Intelectual, AnimoDeprimido, SomaticosMusculares, SomaticosSensoriales,
        Cardiovasculares, Respiratorios, Gastrointestinales, Genitourinarios, Autonomos
    ]
    return _calculate_class_prob('Ansiedad', inputs)
