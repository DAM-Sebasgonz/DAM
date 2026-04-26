<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html lang="es">
            <head>
                <meta charset="UTF-8"/>
                <title>Auditoría Kinart Chronicles</title>
                <style>
                    body { font-family: sans-serif; background: #121212; color: #e0e0e0; padding: 20px; }
                    h1, h2, h3 { color: #f39c12; }
                    section { background: #1e1e1e; margin-bottom: 20px; padding: 15px; border-radius: 8px; border: 1px solid #333; }
                    table { width: 100%; border-collapse: collapse; margin-top: 10px; background: #252525; }
                    th, td { border: 1px solid #444; padding: 10px; text-align: left; }
                    th { background-color: #333; color: #f39c12; }
                    .text-danger { color: #e74c3c; font-weight: bold; }
                    .text-benefit { color: #2ecc71; font-weight: bold; }
                    .item-roto { background-color: #000000; color: #ffffff; }
                    .error-log { border-left: 5px solid #c0392b; background: #2c1a1a; padding: 10px; }
                    footer { margin-top: 30px; padding: 20px; border-top: 2px solid #f39c12; }
                </style>
            </head>
            <body>
                <h1>Kinart Chronicles</h1>
                
                <xsl:apply-templates select="save_data/meta_data"/>
                <xsl:apply-templates select="save_data/character"/>
                <xsl:apply-templates select="save_data/inventory"/>
                <xsl:apply-templates select="save_data/quest_log"/>
                <xsl:apply-templates select="save_data/loadout"/>
                
                <footer>
                    <h2>Resumen de Telemetría</h2>
                    <p>Total XP Acumulada: <strong><xsl:value-of select="sum(//skill/@xp)"/></strong></p>
                    <p>Ratio de Bajas/Muertes: 
                        <strong>
                            <xsl:variable name="deaths" select="save_data/statistics/combat_stats/deaths"/>
                            <xsl:choose>
                                <xsl:when test="$deaths > 0">
                                    <xsl:value-of select="format-number(save_data/statistics/combat_stats/enemies_defeated div $deaths, '0.00')"/>
                                </xsl:when>
                                <xsl:otherwise><xsl:value-of select="save_data/statistics/combat_stats/enemies_defeated"/></xsl:otherwise>
                            </xsl:choose>
                        </strong>
                    </p>
                    <p>Balance Económico Neto: 
                        <strong><xsl:value-of select="save_data/statistics/resource_stats/total_gold_earned - save_data/statistics/resource_stats/total_gold_spent"/></strong>
                    </p>
                </footer>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="meta_data">
        <section>
            <h2>Información de Sesión</h2>
            <p><strong>Héroe:</strong> <xsl:value-of select="char_name"/></p>
            <p><strong>Nivel:</strong> <xsl:value-of select="level"/></p>
            <p><strong>Ubicación:</strong> <xsl:value-of select="last_location/@zone"/></p>
            <p><strong>Tiempo:</strong> 
                <xsl:variable name="raw" select="playtime/simulated/@raw_seconds"/>
                <xsl:value-of select="floor($raw div 3600)"/>h 
                <xsl:value-of select="floor(($raw mod 3600) div 60)"/>m
            </p>
        </section>
    </xsl:template>

    <xsl:template match="character">
        <section>
            <h3>Estado y Habilidades</h3>
            <ul>
                <xsl:for-each select="status_effects/effect[@active='true']">
                    <li>
                        <xsl:attribute name="class">
                            <xsl:choose>
                                <xsl:when test="@id='Bleeding' or @id='Poison' or @id='Burning'">text-danger</xsl:when>
                                <xsl:when test="@id='Cosiness' or @id='WellRested'">text-benefit</xsl:when>
                            </xsl:choose>
                        </xsl:attribute>
                        <xsl:value-of select="@id"/>
                    </li>
                </xsl:for-each>
            </ul>
            <table>
                <tr><th>Habilidad</th><th>Nivel</th><th>XP</th></tr>
                <xsl:for-each select="skills/skill">
                    <xsl:sort select="@level" data-type="number" order="descending"/>
                    <tr>
                        <td><xsl:value-of select="@id"/></td>
                        <td><xsl:value-of select="@level"/></td>
                        <td><xsl:value-of select="@xp"/></td>
                    </tr>
                </xsl:for-each>
            </table>
        </section>
    </xsl:template>

    <xsl:template match="inventory">
        <section>
            <h3>Inventario</h3>
            <table>
                <tr><th>Objeto</th><th>Categoría</th><th>Rareza</th><th>Cant.</th></tr>
                <xsl:for-each select="item">
                    <xsl:sort select="name"/>
                    <tr>
                        <xsl:if test="durability/@current = 0">
                            <xsl:attribute name="class">item-roto</xsl:attribute>
                        </xsl:if>
                        <td>
                            <xsl:value-of select="name"/>
                            <xsl:if test="durability/@current = 0"> [ROTO]</xsl:if>
                            <xsl:if test="@guid = preceding-sibling::item[1]/@guid">
                                <span style="color:#f1c40f"> [!]</span>
                            </xsl:if>
                        </td>
                        <td><xsl:value-of select="substring-before(@item_data, '_')"/></td>
                        <td><xsl:value-of select="rarity"/></td>
                        <td>
                            <xsl:choose>
                                <xsl:when test="@count"><xsl:value-of select="@count"/></xsl:when>
                                <xsl:otherwise>1</xsl:otherwise>
                            </xsl:choose>
                        </td>
                    </tr>
                </xsl:for-each>
            </table>
        </section>
    </xsl:template>

    <xsl:template match="quest_log">
        <section class="error-log">
            <h3>Softlocks Detectados</h3>
            <xsl:for-each select="quest[@state='completed']/variables/variable[@value='false']">
                <p>Error en misión: <xsl:value-of select="../../@title"/> (Variable: <xsl:value-of select="@name"/>)</p>
            </xsl:for-each>
        </section>
    </xsl:template>

    <xsl:template match="loadout">
        <section>
            <h3>Equipamiento</h3>
            <xsl:for-each select="slot[guid]">
                <xsl:variable name="matchGuid" select="guid"/>
                <p>
                    <strong><xsl:value-of select="@id"/>:</strong> <xsl:value-of select="name"/> | 
                    Rareza: <xsl:value-of select="/save_data/inventory/item[@guid = $matchGuid]/rarity"/>
                </p>
            </xsl:for-each>
        </section>
    </xsl:template>
</xsl:stylesheet>