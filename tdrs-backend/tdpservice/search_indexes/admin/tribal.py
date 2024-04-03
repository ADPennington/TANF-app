"""ModelAdmin classes for parsed TRIBAL data files."""
from .filters import CreationDateFilter, FiscalPeriodFilter, STTFilter
from .mixins import ExportCsvMixin, SttCodeMixin, ReadOnlyAdmin


class Tribal_TANF_T1Admin(ReadOnlyAdmin, ExportCsvMixin, SttCodeMixin):
    """ModelAdmin class for parsed Tribal_T1 data files."""

    actions = ["export_as_csv"]
    ordering = ['datafile__stt__stt_code']

    list_display = [
        'RecordType',
        'RPT_MONTH_YEAR',
        'CASE_NUMBER',
        'COUNTY_FIPS_CODE',
        'ZIP_CODE',
        'STRATUM',
        'datafile',
        'stt_code',
    ]

    list_filter = [
        FiscalPeriodFilter,
        CreationDateFilter,
        STTFilter,
        'RPT_MONTH_YEAR',
        'ZIP_CODE',
        'STRATUM',
    ]


class Tribal_TANF_T2Admin(ReadOnlyAdmin, ExportCsvMixin, SttCodeMixin):
    """ModelAdmin class for parsed Tribal_T2 data files."""

    actions = ["export_as_csv"]
    ordering = ['datafile__stt__stt_code']

    list_display = [
        'RecordType',
        'RPT_MONTH_YEAR',
        'CASE_NUMBER',
        'datafile',
        'stt_code',
    ]

    list_filter = [
        FiscalPeriodFilter,
        CreationDateFilter,
        STTFilter,
        'RPT_MONTH_YEAR',
    ]


class Tribal_TANF_T3Admin(ReadOnlyAdmin, ExportCsvMixin, SttCodeMixin):
    """ModelAdmin class for parsed Tribal_T3 data files."""

    actions = ["export_as_csv"]
    ordering = ['datafile__stt__stt_code']

    list_display = [
        'RecordType',
        'RPT_MONTH_YEAR',
        'CASE_NUMBER',
        'datafile',
        'stt_code',
    ]

    list_filter = [
        FiscalPeriodFilter,
        CreationDateFilter,
        STTFilter,
        'RPT_MONTH_YEAR',
    ]

class Tribal_TANF_T4Admin(ReadOnlyAdmin, ExportCsvMixin, SttCodeMixin):
    """ModelAdmin class for parsed Tribal_T4 data files."""

    actions = ["export_as_csv"]
    ordering = ['datafile__stt__stt_code']

    list_display = [
        'RecordType',
        'RPT_MONTH_YEAR',
        'CASE_NUMBER',
        'datafile',
        'stt_code',
    ]

    list_filter = [
        FiscalPeriodFilter,
        CreationDateFilter,
        STTFilter,
        'RPT_MONTH_YEAR',
    ]
class Tribal_TANF_T5Admin(ReadOnlyAdmin, ExportCsvMixin, SttCodeMixin):
    """ModelAdmin class for parsed Tribal_T5 data files."""

    actions = ["export_as_csv"]
    ordering = ['datafile__stt__stt_code']

    list_display = [
        'RecordType',
        'RPT_MONTH_YEAR',
        'CASE_NUMBER',
        'datafile',
        'stt_code',
    ]

    list_filter = [
        FiscalPeriodFilter,
        CreationDateFilter,
        STTFilter,
        'RPT_MONTH_YEAR',
    ]

class Tribal_TANF_T6Admin(ReadOnlyAdmin, ExportCsvMixin, SttCodeMixin):
    """ModelAdmin class for parsed Tribal T6 data files."""

    actions = ["export_as_csv"]
    ordering = ['datafile__stt__stt_code']

    list_display = [
        'RecordType',
        'CALENDAR_QUARTER',
        'RPT_MONTH_YEAR',
        'datafile',
        'stt_code',
    ]

    list_filter = [
        'CALENDAR_QUARTER',
        FiscalPeriodFilter,
        CreationDateFilter,
        STTFilter,
        'RPT_MONTH_YEAR'
    ]

class Tribal_TANF_T7Admin(ReadOnlyAdmin, ExportCsvMixin, SttCodeMixin):
    """ModelAdmin class for parsed Tribal T7 data files."""

    actions = ["export_as_csv"]
    ordering = ['datafile__stt__stt_code']

    list_display = [
        'RecordType',
        'CALENDAR_QUARTER',
        'RPT_MONTH_YEAR',
        'TDRS_SECTION_IND',
        'STRATUM',
        'FAMILIES_MONTH',
        'datafile',
        'stt_code',
    ]

    list_filter = [
        'CALENDAR_QUARTER',
        FiscalPeriodFilter,
        CreationDateFilter,
        STTFilter,
        'RPT_MONTH_YEAR',
    ]
