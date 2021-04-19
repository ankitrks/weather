# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

sample_response = {
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [
            -0.25,
            51.5,
            9
        ]
    },
    "properties": {
        "meta": {
            "updated_at": "2021-04-19T09:39:51Z",
            "units": {
                "air_pressure_at_sea_level": "hPa",
                "air_temperature": "celsius",
                "cloud_area_fraction": "%",
                "precipitation_amount": "mm",
                "relative_humidity": "%",
                "wind_from_direction": "degrees",
                "wind_speed": "m/s"
            }
        },
        "timeseries": [
            {
                "time": "2021-04-19T13:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1020.8,
                            "air_temperature": 15.1,
                            "cloud_area_fraction": 78.9,
                            "relative_humidity": 51.2,
                            "wind_from_direction": 109.4,
                            "wind_speed": 2.2
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T14:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1020.1,
                            "air_temperature": 15.4,
                            "cloud_area_fraction": 96.1,
                            "relative_humidity": 49.0,
                            "wind_from_direction": 100.1,
                            "wind_speed": 2.2
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T15:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.4,
                            "air_temperature": 15.3,
                            "cloud_area_fraction": 83.6,
                            "relative_humidity": 49.5,
                            "wind_from_direction": 89.1,
                            "wind_speed": 2.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T16:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.0,
                            "air_temperature": 15.2,
                            "cloud_area_fraction": 82.8,
                            "relative_humidity": 49.5,
                            "wind_from_direction": 75.8,
                            "wind_speed": 2.3
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T17:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.9,
                            "air_temperature": 14.6,
                            "cloud_area_fraction": 81.2,
                            "relative_humidity": 52.7,
                            "wind_from_direction": 77.7,
                            "wind_speed": 2.7
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.9,
                            "air_temperature": 13.5,
                            "cloud_area_fraction": 61.7,
                            "relative_humidity": 59.8,
                            "wind_from_direction": 111.9,
                            "wind_speed": 2.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T19:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.1,
                            "air_temperature": 11.6,
                            "cloud_area_fraction": 51.6,
                            "relative_humidity": 66.8,
                            "wind_from_direction": 140.0,
                            "wind_speed": 2.5
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T20:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.4,
                            "air_temperature": 9.5,
                            "cloud_area_fraction": 20.3,
                            "relative_humidity": 82.7,
                            "wind_from_direction": 180.1,
                            "wind_speed": 2.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T21:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.5,
                            "air_temperature": 8.0,
                            "cloud_area_fraction": 8.6,
                            "relative_humidity": 87.2,
                            "wind_from_direction": 144.8,
                            "wind_speed": 1.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T22:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.6,
                            "air_temperature": 6.7,
                            "cloud_area_fraction": 11.7,
                            "relative_humidity": 91.9,
                            "wind_from_direction": 87.2,
                            "wind_speed": 1.4
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-19T23:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.5,
                            "air_temperature": 4.7,
                            "cloud_area_fraction": 8.6,
                            "relative_humidity": 97.0,
                            "wind_from_direction": 94.9,
                            "wind_speed": 1.7
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T00:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.4,
                            "air_temperature": 4.0,
                            "cloud_area_fraction": 7.0,
                            "relative_humidity": 97.9,
                            "wind_from_direction": 76.4,
                            "wind_speed": 1.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T01:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.0,
                            "air_temperature": 3.8,
                            "cloud_area_fraction": 16.4,
                            "relative_humidity": 97.0,
                            "wind_from_direction": 73.8,
                            "wind_speed": 1.3
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T02:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.5,
                            "air_temperature": 3.2,
                            "cloud_area_fraction": 18.7,
                            "relative_humidity": 96.2,
                            "wind_from_direction": 63.5,
                            "wind_speed": 1.5
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T03:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.3,
                            "air_temperature": 3.0,
                            "cloud_area_fraction": 6.2,
                            "relative_humidity": 96.7,
                            "wind_from_direction": 58.1,
                            "wind_speed": 1.3
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T04:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.1,
                            "air_temperature": 2.9,
                            "cloud_area_fraction": 3.1,
                            "relative_humidity": 96.4,
                            "wind_from_direction": 63.1,
                            "wind_speed": 1.4
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T05:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.3,
                            "air_temperature": 2.7,
                            "cloud_area_fraction": 83.6,
                            "relative_humidity": 98.7,
                            "wind_from_direction": 70.0,
                            "wind_speed": 1.4
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T06:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.5,
                            "air_temperature": 3.8,
                            "cloud_area_fraction": 91.4,
                            "relative_humidity": 97.8,
                            "wind_from_direction": 71.3,
                            "wind_speed": 1.4
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T07:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.6,
                            "air_temperature": 5.7,
                            "cloud_area_fraction": 90.6,
                            "relative_humidity": 93.4,
                            "wind_from_direction": 78.5,
                            "wind_speed": 0.9
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T08:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.5,
                            "air_temperature": 8.6,
                            "cloud_area_fraction": 20.3,
                            "relative_humidity": 83.0,
                            "wind_from_direction": 61.7,
                            "wind_speed": 1.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.1
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T09:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.4,
                            "air_temperature": 11.5,
                            "cloud_area_fraction": 74.2,
                            "relative_humidity": 71.2,
                            "wind_from_direction": 55.3,
                            "wind_speed": 1.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.2
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T10:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.2,
                            "air_temperature": 13.4,
                            "cloud_area_fraction": 86.7,
                            "relative_humidity": 61.9,
                            "wind_from_direction": 52.7,
                            "wind_speed": 2.2
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.2
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T11:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.0,
                            "air_temperature": 14.6,
                            "cloud_area_fraction": 35.2,
                            "relative_humidity": 54.6,
                            "wind_from_direction": 59.9,
                            "wind_speed": 2.2
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.2
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.6,
                            "air_temperature": 15.1,
                            "cloud_area_fraction": 66.4,
                            "relative_humidity": 50.1,
                            "wind_from_direction": 68.1,
                            "wind_speed": 2.2
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.2
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T13:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.3,
                            "air_temperature": 15.2,
                            "cloud_area_fraction": 74.2,
                            "relative_humidity": 49.8,
                            "wind_from_direction": 79.2,
                            "wind_speed": 2.3
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.1
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.2
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T14:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.1,
                            "air_temperature": 15.2,
                            "cloud_area_fraction": 68.7,
                            "relative_humidity": 51.2,
                            "wind_from_direction": 79.5,
                            "wind_speed": 2.1
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.1
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.1
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T15:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1016.7,
                            "air_temperature": 15.0,
                            "cloud_area_fraction": 68.0,
                            "relative_humidity": 52.8,
                            "wind_from_direction": 76.5,
                            "wind_speed": 2.2
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T16:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1016.4,
                            "air_temperature": 14.4,
                            "cloud_area_fraction": 52.3,
                            "relative_humidity": 56.8,
                            "wind_from_direction": 85.9,
                            "wind_speed": 2.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T17:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1016.5,
                            "air_temperature": 14.1,
                            "cloud_area_fraction": 42.2,
                            "relative_humidity": 58.5,
                            "wind_from_direction": 84.0,
                            "wind_speed": 2.3
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1016.6,
                            "air_temperature": 13.3,
                            "cloud_area_fraction": 42.2,
                            "relative_humidity": 66.3,
                            "wind_from_direction": 101.0,
                            "wind_speed": 1.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T19:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1016.7,
                            "air_temperature": 11.0,
                            "cloud_area_fraction": 44.5,
                            "relative_humidity": 75.4,
                            "wind_from_direction": 103.9,
                            "wind_speed": 1.8
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T20:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.2,
                            "air_temperature": 9.7,
                            "cloud_area_fraction": 47.7,
                            "relative_humidity": 82.3,
                            "wind_from_direction": 91.8,
                            "wind_speed": 1.8
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T21:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.6,
                            "air_temperature": 8.2,
                            "cloud_area_fraction": 64.8,
                            "relative_humidity": 89.0,
                            "wind_from_direction": 104.1,
                            "wind_speed": 1.7
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T22:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.8,
                            "air_temperature": 7.4,
                            "cloud_area_fraction": 68.7,
                            "relative_humidity": 91.4,
                            "wind_from_direction": 97.3,
                            "wind_speed": 1.8
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-20T23:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.8,
                            "air_temperature": 6.9,
                            "cloud_area_fraction": 71.9,
                            "relative_humidity": 91.0,
                            "wind_from_direction": 87.2,
                            "wind_speed": 1.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T00:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.8,
                            "air_temperature": 6.9,
                            "cloud_area_fraction": 82.8,
                            "relative_humidity": 90.4,
                            "wind_from_direction": 67.0,
                            "wind_speed": 1.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T01:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.6,
                            "air_temperature": 5.8,
                            "cloud_area_fraction": 87.5,
                            "relative_humidity": 94.8,
                            "wind_from_direction": 50.1,
                            "wind_speed": 1.5
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T02:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.3,
                            "air_temperature": 5.5,
                            "cloud_area_fraction": 92.2,
                            "relative_humidity": 96.4,
                            "wind_from_direction": 47.2,
                            "wind_speed": 1.8
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T03:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.2,
                            "air_temperature": 5.5,
                            "cloud_area_fraction": 96.1,
                            "relative_humidity": 96.7,
                            "wind_from_direction": 45.9,
                            "wind_speed": 1.9
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T04:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.3,
                            "air_temperature": 5.1,
                            "cloud_area_fraction": 64.1,
                            "relative_humidity": 97.9,
                            "wind_from_direction": 51.0,
                            "wind_speed": 2.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T05:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1017.5,
                            "air_temperature": 4.5,
                            "cloud_area_fraction": 50.0,
                            "relative_humidity": 98.1,
                            "wind_from_direction": 28.5,
                            "wind_speed": 2.3
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T06:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.1,
                            "air_temperature": 6.8,
                            "cloud_area_fraction": 33.6,
                            "relative_humidity": 91.8,
                            "wind_from_direction": 18.3,
                            "wind_speed": 2.7
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T07:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1018.9,
                            "air_temperature": 9.0,
                            "cloud_area_fraction": 28.1,
                            "relative_humidity": 84.8,
                            "wind_from_direction": 27.7,
                            "wind_speed": 4.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T08:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1019.5,
                            "air_temperature": 10.0,
                            "cloud_area_fraction": 46.9,
                            "relative_humidity": 78.2,
                            "wind_from_direction": 33.9,
                            "wind_speed": 4.8
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T09:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1020.1,
                            "air_temperature": 10.9,
                            "cloud_area_fraction": 96.1,
                            "relative_humidity": 70.7,
                            "wind_from_direction": 40.7,
                            "wind_speed": 5.8
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T10:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1020.7,
                            "air_temperature": 10.9,
                            "cloud_area_fraction": 99.2,
                            "relative_humidity": 70.9,
                            "wind_from_direction": 40.3,
                            "wind_speed": 5.9
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T11:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1021.2,
                            "air_temperature": 10.3,
                            "cloud_area_fraction": 100.0,
                            "relative_humidity": 71.6,
                            "wind_from_direction": 44.9,
                            "wind_speed": 6.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1021.7,
                            "air_temperature": 9.5,
                            "cloud_area_fraction": 99.2,
                            "relative_humidity": 69.8,
                            "wind_from_direction": 44.4,
                            "wind_speed": 6.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T13:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1022.1,
                            "air_temperature": 9.3,
                            "cloud_area_fraction": 100.0,
                            "relative_humidity": 61.8,
                            "wind_from_direction": 44.2,
                            "wind_speed": 5.5
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T14:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1022.1,
                            "air_temperature": 9.6,
                            "cloud_area_fraction": 100.0,
                            "relative_humidity": 56.4,
                            "wind_from_direction": 45.2,
                            "wind_speed": 4.8
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T15:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1021.9,
                            "air_temperature": 10.2,
                            "cloud_area_fraction": 85.2,
                            "relative_humidity": 55.9,
                            "wind_from_direction": 48.1,
                            "wind_speed": 4.0
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T16:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1021.5,
                            "air_temperature": 11.6,
                            "cloud_area_fraction": 30.5,
                            "relative_humidity": 49.1,
                            "wind_from_direction": 37.4,
                            "wind_speed": 4.6
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T17:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1021.9,
                            "air_temperature": 11.0,
                            "cloud_area_fraction": 9.4,
                            "relative_humidity": 49.8,
                            "wind_from_direction": 31.6,
                            "wind_speed": 5.3
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1022.3,
                            "air_temperature": 9.6,
                            "cloud_area_fraction": 20.3,
                            "relative_humidity": 51.1,
                            "wind_from_direction": 29.9,
                            "wind_speed": 5.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T19:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1023.0,
                            "air_temperature": 7.7,
                            "cloud_area_fraction": 0.0,
                            "relative_humidity": 53.7,
                            "wind_from_direction": 29.1,
                            "wind_speed": 4.7
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T20:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1024.0,
                            "air_temperature": 6.3,
                            "cloud_area_fraction": 0.0,
                            "relative_humidity": 58.5,
                            "wind_from_direction": 31.8,
                            "wind_speed": 4.6
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T21:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1024.8,
                            "air_temperature": 5.2,
                            "cloud_area_fraction": 14.8,
                            "relative_humidity": 62.8,
                            "wind_from_direction": 37.3,
                            "wind_speed": 4.1
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T22:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1025.5,
                            "air_temperature": 4.1,
                            "cloud_area_fraction": 8.6,
                            "relative_humidity": 66.4,
                            "wind_from_direction": 36.6,
                            "wind_speed": 3.8
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-21T23:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1025.9,
                            "air_temperature": 2.9,
                            "cloud_area_fraction": 12.5,
                            "relative_humidity": 73.1,
                            "wind_from_direction": 37.6,
                            "wind_speed": 2.8
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-22T00:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1026.1,
                            "air_temperature": 2.1,
                            "cloud_area_fraction": 56.2,
                            "relative_humidity": 78.5,
                            "wind_from_direction": 38.0,
                            "wind_speed": 2.2
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-22T06:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1026.7,
                            "air_temperature": 2.3,
                            "cloud_area_fraction": 0.8,
                            "relative_humidity": 80.0,
                            "wind_from_direction": 10.6,
                            "wind_speed": 2.8
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-22T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1027.4,
                            "air_temperature": 11.8,
                            "cloud_area_fraction": 41.4,
                            "relative_humidity": 45.1,
                            "wind_from_direction": 43.7,
                            "wind_speed": 4.3
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "clearsky_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-22T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1026.8,
                            "air_temperature": 11.1,
                            "cloud_area_fraction": 0.0,
                            "relative_humidity": 51.5,
                            "wind_from_direction": 40.4,
                            "wind_speed": 2.7
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-23T00:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1028.7,
                            "air_temperature": 1.9,
                            "cloud_area_fraction": 0.0,
                            "relative_humidity": 88.4,
                            "wind_from_direction": 97.9,
                            "wind_speed": 2.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-23T06:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1029.4,
                            "air_temperature": 2.0,
                            "cloud_area_fraction": 5.5,
                            "relative_humidity": 90.1,
                            "wind_from_direction": 45.1,
                            "wind_speed": 1.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-23T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1029.2,
                            "air_temperature": 12.8,
                            "cloud_area_fraction": 54.7,
                            "relative_humidity": 50.0,
                            "wind_from_direction": 61.3,
                            "wind_speed": 4.5
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-23T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1028.1,
                            "air_temperature": 11.4,
                            "cloud_area_fraction": 32.8,
                            "relative_humidity": 54.9,
                            "wind_from_direction": 58.9,
                            "wind_speed": 4.2
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-24T00:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1030.3,
                            "air_temperature": 3.5,
                            "cloud_area_fraction": 28.1,
                            "relative_humidity": 93.6,
                            "wind_from_direction": 65.5,
                            "wind_speed": 2.5
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-24T06:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1030.4,
                            "air_temperature": 3.7,
                            "cloud_area_fraction": 25.0,
                            "relative_humidity": 91.0,
                            "wind_from_direction": 44.0,
                            "wind_speed": 3.3
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-24T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1030.7,
                            "air_temperature": 9.7,
                            "cloud_area_fraction": 100.0,
                            "relative_humidity": 57.1,
                            "wind_from_direction": 57.1,
                            "wind_speed": 4.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-24T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1029.6,
                            "air_temperature": 9.3,
                            "cloud_area_fraction": 80.5,
                            "relative_humidity": 53.3,
                            "wind_from_direction": 61.4,
                            "wind_speed": 5.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-25T00:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1031.1,
                            "air_temperature": 3.6,
                            "cloud_area_fraction": 16.4,
                            "relative_humidity": 74.9,
                            "wind_from_direction": 51.0,
                            "wind_speed": 3.5
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "fair_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-25T06:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1030.2,
                            "air_temperature": 3.6,
                            "cloud_area_fraction": 47.7,
                            "relative_humidity": 87.7,
                            "wind_from_direction": 40.0,
                            "wind_speed": 2.9
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-25T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1028.9,
                            "air_temperature": 10.7,
                            "cloud_area_fraction": 84.4,
                            "relative_humidity": 57.0,
                            "wind_from_direction": 53.2,
                            "wind_speed": 4.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "clearsky_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-25T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1025.7,
                            "air_temperature": 10.0,
                            "cloud_area_fraction": 18.7,
                            "relative_humidity": 63.6,
                            "wind_from_direction": 88.5,
                            "wind_speed": 3.7
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-26T00:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1025.0,
                            "air_temperature": 2.5,
                            "cloud_area_fraction": 0.0,
                            "relative_humidity": 89.9,
                            "wind_from_direction": 66.8,
                            "wind_speed": 1.7
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "clearsky_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-26T06:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1021.4,
                            "air_temperature": 2.9,
                            "cloud_area_fraction": 7.8,
                            "relative_humidity": 93.3,
                            "wind_from_direction": 321.9,
                            "wind_speed": 0.9
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "clearsky_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-26T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1016.4,
                            "air_temperature": 13.6,
                            "cloud_area_fraction": 3.1,
                            "relative_humidity": 52.1,
                            "wind_from_direction": 267.1,
                            "wind_speed": 0.6
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-26T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1011.2,
                            "air_temperature": 14.4,
                            "cloud_area_fraction": 87.5,
                            "relative_humidity": 47.1,
                            "wind_from_direction": 341.2,
                            "wind_speed": 2.7
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-27T00:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1012.0,
                            "air_temperature": 6.8,
                            "cloud_area_fraction": 78.1,
                            "relative_humidity": 75.5,
                            "wind_from_direction": 350.5,
                            "wind_speed": 2.1
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-27T06:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1012.8,
                            "air_temperature": 5.8,
                            "cloud_area_fraction": 25.0,
                            "relative_humidity": 87.3,
                            "wind_from_direction": 14.4,
                            "wind_speed": 4.5
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-27T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1013.6,
                            "air_temperature": 9.9,
                            "cloud_area_fraction": 90.6,
                            "relative_humidity": 56.9,
                            "wind_from_direction": 0.7,
                            "wind_speed": 4.9
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_day"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-27T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1013.3,
                            "air_temperature": 9.2,
                            "cloud_area_fraction": 86.7,
                            "relative_humidity": 50.0,
                            "wind_from_direction": 11.2,
                            "wind_speed": 4.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-28T00:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1014.7,
                            "air_temperature": 4.0,
                            "cloud_area_fraction": 25.8,
                            "relative_humidity": 75.8,
                            "wind_from_direction": 337.7,
                            "wind_speed": 2.5
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "partlycloudy_night"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-28T06:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1014.3,
                            "air_temperature": 4.8,
                            "cloud_area_fraction": 86.7,
                            "relative_humidity": 78.4,
                            "wind_from_direction": 354.9,
                            "wind_speed": 3.0
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.1
                        }
                    }
                }
            },
            {
                "time": "2021-04-28T12:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1014.0,
                            "air_temperature": 10.8,
                            "cloud_area_fraction": 100.0,
                            "relative_humidity": 45.9,
                            "wind_from_direction": 9.1,
                            "wind_speed": 1.7
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            },
            {
                "time": "2021-04-28T18:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1012.4,
                            "air_temperature": 10.8,
                            "cloud_area_fraction": 93.7,
                            "relative_humidity": 48.7,
                            "wind_from_direction": 72.4,
                            "wind_speed": 1.0
                        }
                    }
                }
            }
        ]
    }
}

def index(request):
	return render(request, 'index.html', {})

@csrf_exempt
def ajax_weather_data(request):
	data = {'status' : 'success'}
	try:
		c_lat = request.GET.get('lat')
		c_long = request.GET.get('long')
		# url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=' + c_lat + '&lon=' + c_long
		
		# using hard-coded url as most of the location are returning 403s
		url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=51.5&lon=-0.25'
		response = requests.get(url).json()
		data['w_data'] = response
	except Exception as e:
		# Send sample response bbecause of the API limitations...
		data = {'status' : 'fail', 'message' : 'Could not find the location', 'w_data' : sample_response}
	return JsonResponse(data) 